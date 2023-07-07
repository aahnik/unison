from django.urls import path

from . import views

app_name = "donations"

urlpatterns = [
    path("", views.donations, name="donations"),
    path("donate/", views.make_donation, name="make_donation"),
    path("success/", views.success_page, name="success_page"),
    path("failure/", views.failure_page, name="failure_page"),
    path("payment-status/", views.payment_status, name="payment_status"),
]
