from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventRegistration
import logging
import json


log = logging.getLogger(__name__)


def haps_list(request: HttpRequest):
    haps = Event.objects.all()
    context = {"haps": haps}
    return render(request, "haps/list.html", context=context)


def haps_item(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    context = {"hap": event}

    return render(request, "haps/item.html", context=context)


@login_required(login_url="/users/register")
def register_for_event(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    
    if not event.accept_reg:
        messages.error(request, "Registration is closed for this event.")
        return redirect('haps:item', slug=slug)

    if event.login_required and not request.user.is_authenticated:
        messages.error(request, "Please login to register for this event.")
        return redirect('users:register')

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
        registration = EventRegistration.objects.create(
            event=event,
            user=request.user if event.login_required else None,
            form_responses=form_responses,
            amount=event.registration_fee
        )
        
        # If payment required, redirect to payment page
        if event.registration_fee:
            # TODO: Implement payment flow using donations module
            return redirect('donations:payment', registration_id=registration.id)
        
        messages.success(request, "Successfully registered for the event!")
        return render(request, "haps/register_success.html", 
                     context={"event": event, "registration": registration})
    
    # If GET request with registration modal, return to event page
    return redirect('haps:item', slug=slug)
