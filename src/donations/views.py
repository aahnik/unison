from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import DonationConfig, DonationTier

# Create your views here.


def donations(request):
    donation_config = DonationConfig.get_solo()
    donation_tiers = DonationTier.objects.all()
    context = {"donation_config": donation_config, "donation_tiers": donation_tiers}
    return render(request, "donations/donations.html", context=context)


def donation_success_page(request):
    return render(request, "donations/success.html")


def donation_failure_page(request):
    return render(request, "donations/failure.html")


def payment_gateway_callback_handler(request):
    # handle the request made by payment gateway after user has done payment
    pass


def make_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("donations:donation_success_page")
        else:
            print(form.errors)

    else:
        form = DonationForm()
    return render(request, "donations/donation_form.html", {"form": form})
