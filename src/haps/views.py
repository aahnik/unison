from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventRegistration
import logging
import json
from utils.payment.upi_gateway import create_order, check_order_status
from django.urls import reverse
from uuid import uuid4
from datetime import date
from utils.logging import critical_logger

log = logging.getLogger(__name__)


def haps_list(request: HttpRequest):
    haps = Event.objects.all()
    context = {"haps": haps}
    return render(request, "haps/list.html", context=context)


def haps_item(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    context = {"hap": event}

    return render(request, "haps/item.html", context=context)


# @login_required(login_url="/users/register")
def register_for_event(request: HttpRequest, slug: str):
    """Register for an event"""
    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("Event not found")

    if not event.accept_reg:
        messages.error(request, "Registration is closed for this event.")
        return redirect('haps:event_item', slug=slug)

    if event.login_required and not request.user.is_authenticated:
        messages.error(request, "Please login to register for this event.")
        return redirect('haps:event_item', slug=slug)

    if request.method == 'POST':
        # Collect form responses
        form_responses = {}

        # If not login required, collect basic info
        if not event.login_required:
            form_responses['name'] = request.POST.get('name')
            form_responses['whatsapp_number'] = request.POST.get('whatsapp_number')

        # Collect custom field responses
        for field in event.form_fields.all():
            field_id = f'field_{field.id}'
            form_responses[field.field_label] = request.POST.get(field_id)

        # Create registration
        registration = EventRegistration(
            event=event,
            user=request.user if request.user.is_authenticated else None,
            form_responses=form_responses,
            amount=event.registration_fee if event.registration_fee else None
        )
        registration.save()

        # If payment required, redirect to payment page
        if event.registration_fee:
            return redirect('haps:initiate_payment', registration_id=registration.id)

        messages.success(request, "Successfully registered for the event!")
        return render(request, "haps/register_success.html",
                     context={"registration": registration, "event": event})

    # If GET request with registration modal, return to event page
    return redirect('haps:event_item', slug=slug)


def register_failure(request: HttpRequest, registration_id: int):
    """View for displaying registration failure page.
    This is typically shown when payment fails."""

    try:
        registration = EventRegistration.objects.select_related('event', 'user').get(id=registration_id)
    except EventRegistration.DoesNotExist:
        raise Http404("Registration not found")

    # For testing, you can pass a remark through URL query parameter
    remark = request.GET.get('remark', 'Payment was not completed')

    context = {
        "registration": registration,
        "event": registration.event,
        "remark": remark
    }
    return render(request, "haps/register_failure.html", context=context)


def initiate_payment(request: HttpRequest, registration_id: int):
    """Initiate payment for event registration"""
    try:
        registration = EventRegistration.objects.select_related('event', 'user').get(id=registration_id)
    except EventRegistration.DoesNotExist:
        raise Http404("Registration not found")

    # Validate amount
    if not registration.amount:
        log.error(f"Registration {registration.id} has no amount set")
        messages.error(request, "Invalid registration amount")
        return redirect('haps:register_failure', registration_id=registration.id)

    if registration.payment_status == 'success':
        messages.info(request, "Payment already completed")
        return redirect('haps:register_success', registration_id=registration.id)

    # Generate unique transaction ID if not exists
    if not registration.client_txn_id:
        registration.client_txn_id = f"TempleWebPay-event-{registration.id}-{uuid4().hex[:8]}"
        registration.save(update_fields=['client_txn_id'])

    # Create callback URL
    callback_url = request.build_absolute_uri(
        reverse('haps:payment_callback')
    )

    # Get user details
    name = None
    if registration.user:
        name = registration.user.get_full_name()
        if not name:
            name = registration.user.username
    else:
        name = registration.form_responses.get('name')

    if not name:
        log.error(f"Registration {registration.id} has no customer name")

        # return redirect('haps:register_failure', registration_id=registration.id)
        name = "Anonymous User"

    mobile = registration.form_responses.get('whatsapp_number', '')
    email = registration.user.email if registration.user else ''

    try:
        # Create payment order
        status, api_resp = create_order(
            client_txn_id=registration.client_txn_id,
            redirect_url=callback_url,
            amount=registration.amount,
            product_info=f"Registration for {registration.event.name}",
            customer_name=name,
            # customer_email=email,
            # customer_mobile=mobile
        )

        if not status:
            log.error(f"Payment gateway error for registration {registration.id}: {api_resp.text}")
            messages.error(request, "Payment gateway error. Please try again later.")
            return redirect('haps:register_failure',
                          registration_id=registration.id,
                          remark=f"Payment gateway error: {api_resp.text}")

        # Save order ID and redirect to payment URL
        registration.order_id = api_resp["order_id"]
        registration.save(update_fields=['order_id'])

        return redirect(api_resp["payment_url"])

    except Exception as e:
        log.error(f"Payment initiation failed for registration {registration.id}: {str(e)}")
        messages.error(request, "Failed to initiate payment. Please try again.")
        return redirect('haps:register_failure', registration_id=registration.id)


def payment_callback(request: HttpRequest):
    """Handle payment gateway callback"""
    log.debug("Payment callback called")
    client_txn_id = request.GET.get('client_txn_id')
    if not client_txn_id:
        messages.error(request, "Invalid payment callback")
        return redirect('haps:events')

    try:
        registration = EventRegistration.objects.get(client_txn_id=client_txn_id)
    except EventRegistration.DoesNotExist:
        messages.error(request, "Registration not found")
        return redirect('haps:events')

    # Prevent duplicate processing
    if registration.payment_status == 'success':
        return redirect('haps:register_success', registration_id=registration.id)

    # Check payment status
    try:
        status_data = check_order_status(client_txn_id)
        if not status_data:
            raise ValueError("Empty response from payment gateway")

        # Store all payment diagnostic data
        registration.payment_data = {
            'customer_vpa': status_data.get('customer_vpa'),
            'upi_txn_id': status_data.get('upi_txn_id'),
            'status': status_data.get('status'),
            'remark': status_data.get('remark'),
            'txnAt': status_data.get('txnAt'),
            'merchant': status_data.get('Merchant', {}),
            'udf1': status_data.get('udf1'),
            'udf2': status_data.get('udf2'),
            'udf3': status_data.get('udf3'),
            'redirect_url': status_data.get('redirect_url'),
            'createdAt': status_data.get('createdAt')
        }

        # Update payment status
        if status_data['status'] == 'success':
            registration.payment_status = 'success'
            registration.payment_date_time = status_data.get('txnAt')
            registration.save(update_fields=['payment_status', 'payment_date_time', 'payment_data'])
            messages.success(request, "Payment successful!")
            return redirect('haps:register_success', registration_id=registration.id)
        else:
            registration.payment_status = 'failure'
            registration.save(update_fields=['payment_status', 'payment_data'])
            return redirect('haps:register_failure',
                        registration_id=registration.id,
                        remark=status_data.get('remark', 'Payment failed'))

    except Exception as e:
        log.error(f"Payment verification failed for registration {registration.id}: {str(e)}")
        registration.payment_data = {'error': str(e)}
        registration.payment_status = 'failure'
        registration.save(update_fields=['payment_status', 'payment_data'])
        return redirect('haps:register_failure',
                    registration_id=registration.id,
                    remark="Payment verification failed")


def retry_payment(request: HttpRequest, registration_id: int):
    """Retry failed payment"""
    try:
        registration = EventRegistration.objects.get(id=registration_id)
    except EventRegistration.DoesNotExist:
        raise Http404("Registration not found")

    if registration.payment_status == 'success':
        messages.info(request, "Payment already completed")
        return redirect('haps:register_success', registration_id=registration.id)

    # Log critical payment data before reset
    critical_logger.critical(
        f"Payment retry initiated for registration {registration.id}. "
        f"Previous payment data: order_id={registration.order_id}, "
        f"client_txn_id={registration.client_txn_id}, "
        f"payment_status={registration.payment_status}, "
        f"payment_data={registration.payment_data}"
    )

    # Reset payment fields for retry
    registration.order_id = None
    registration.client_txn_id = None
    registration.payment_status = 'pending'
    registration.save(update_fields=['order_id', 'client_txn_id', 'payment_status'])

    return redirect('haps:initiate_payment', registration_id=registration.id)


def register_success(request: HttpRequest, registration_id: int):
    """View for displaying registration success page."""
    try:
        registration = EventRegistration.objects.select_related('event', 'user').get(id=registration_id)
    except EventRegistration.DoesNotExist:
        raise Http404("Registration not found")

    context = {
        "registration": registration,
        "event": registration.event,
    }
    return render(request, "haps/register_success.html", context=context)
