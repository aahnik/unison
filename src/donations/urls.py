from django.urls import path

from . import views

app_name = "donations"

urlpatterns = [
    path("", views.donations, name="donations"),
    path("donate/", views.make_donation, name="make_donation"),
    path("success/", views.donation_success_page, name="donation_success_page"),
    path("failure/", views.donation_failure_page, name="donation_failure_page"),
]
