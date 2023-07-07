from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DonationForm
from .models import DonationConfig, DonationTier, DonationReceived
from temple_web.myconfig import PaymentGatewayConfig
from .upi_gateway import create_order, check_order_status
from uuid import uuid4
from datetime import date
from utils.adirect import adirect
from django.http import HttpRequest, Http404

# Create your views here.
from urllib.parse import urlencode

import logging

logger = logging.getLogger(__name__)


def donations(request):
    donation_config = DonationConfig.get_solo()
    donation_tiers = DonationTier.objects.all()
    context = {"donation_config": donation_config, "donation_tiers": donation_tiers}
    return render(request, "donations/donations.html", context=context)


def success_page(request):
    client_txn_id = request.GET.get("client_txn_id")
    print(client_txn_id)

    try:
        donation_recvd = DonationReceived.objects.get(client_txn_id=client_txn_id)
    except DonationReceived.DoesNotExist:
        logger.error("Client txn id does not exist in db")
        raise Http404("client_txn_id does not exist in database")
    if donation_recvd.payment_status == "success":
        context = {"donation_recvd": donation_recvd}

        return render(request, "donations/success.html", context=context)
    else:
        raise Http404("Success record does not exist for given client_txn_id")


def failure_page(request):
    remark = request.GET.get("remark")
    logging.error("error page called with %s", remark)
    context = {"remark": remark}
    return render(request, "donations/failure.html", context=context)


def payment_status(request):
    #  payment_gateway_callback_handler
    # handle the redirect made by payment gateway after user has done payment
    # check if the payment succeeded, and upate in db
    # display a loading page
    # and then show success or failure
    # if success, then give option to print receipt

    # fetch the query parameters
    client_txn_id = request.GET.get("client_txn_id")
    order_id = request.GET.get("txn_id")

    # fetch the donation record from db
    donation_recvd = DonationReceived.objects.get(client_txn_id=client_txn_id)

    # integrity check
    if donation_recvd.order_id == order_id:
        # call Payment Gateway API for order status
        tdate = donation_recvd.payment_date_time.date()
        resp = check_order_status(client_txn_id=client_txn_id, txn_date=tdate)
        # if we get valid response
        if resp is not None:
            # store the remark and status in the db
            donation_recvd.remark = resp["remark"]
            donation_recvd.payment_status = resp["status"]

            if resp["status"] == "success":
                # in case of success store more details in db
                donation_recvd.upi_tranaction_id = resp["upi_txn_id"]
                donation_recvd.customer_vpa = resp["customer_vpa"]
                donation_recvd.merchant_name = resp["Merchant"]["name"]
                donation_recvd.merchant_upi_id = resp["Merchant"]["upi_id"]
                donation_recvd.save()
                # save back to db, and redirect to success page
                return adirect(
                    "donations:success_page",
                    client_txn_id=donation_recvd.client_txn_id,
                )

            else:
                donation_recvd.save()
                logger.warning("Payment failed! %s", resp["remark"])
                # return redirect(
                #     reverse("donations:failure_page"), remark=resp["remark"]
                # )
                return adirect("donations:failure_page", remark=resp["remark"])
        else:
            logging.warning("Could not check order status!")
            return adirect(
                "donations:failure_page",
                remark=f"Payment Gateway {PaymentGatewayConfig.CHECK_ORDER_STATUS} refused to connect",
            )

    else:
        logger.warning(
            "Integrity Error! order_id fetched from db for client_txn_id does not match order_id returned by UPI Gateway"
        )
        return adirect(
            "donations:failure_page",
            remark="Order IDs dont match. Integrity Error!",
        )


def get_callback_url(request: HttpRequest):
    protocol = request.scheme
    host = request.get_host()
    cburl = f"{protocol}://{host}/donations/payment-status"
    print("from get_callback_url function", cburl)
    return cburl


def make_donation(request: HttpRequest):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation_recvd: DonationReceived = form.save(commit=False)
            # make api call
            tdate = date.today()
            client_txn_id = "TempleWebPay-" + str(tdate) + "-" + str(uuid4())
            donation_recvd.client_txn_id = client_txn_id

            status, api_resp = create_order(
                client_txn_id=client_txn_id,
                redirect_url=get_callback_url(request),
                amount=donation_recvd.amount,
                product_info=donation_recvd.donation_tier.name,
                customer_name=donation_recvd.name,
                customer_mobile=donation_recvd.whatsapp_number,
            )
            if not status:
                # redirect to failure page
                # and pass the context that payment gateway error
                # refused to connect
                # try again
                # if persists, contact admins
                return adirect("donations:failure_page", remark=api_resp.text)

            # TODO: getting a remark None here

            else:
                donation_recvd.order_id = api_resp["order_id"]

            donation_recvd.save()
            # save client_txn_id to db
            # and after api responds, save order id

            # redirect to payment page

            return redirect(api_resp["payment_url"])
        else:
            print(form.errors)

    else:
        tier_id = request.GET.get("tier")
        pre_filled_data = {}
        if tier_id is not None:
            try:
                donation_tier = DonationTier.objects.get(id=tier_id)
            except DonationTier.DoesNotExist:
                raise Http404("This donation tier does not exist. Try again.")

            pre_filled_data.update(
                {
                    "donation_tier": donation_tier.pk,
                    "amount": donation_tier.amount,
                }
            )
        form = DonationForm(initial=pre_filled_data)
    return render(request, "donations/donation_form.html", {"form": form})
