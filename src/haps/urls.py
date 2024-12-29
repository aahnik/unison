from django.urls import path

from . import views

app_name = "haps"

urlpatterns = [
    path("", views.haps_list, name="events"),
    path("<slug:slug>", views.haps_item, name="event_item"),
    path("<slug:slug>/register", views.register_for_event, name="register"),
    path("registration/<int:registration_id>/failure", views.register_failure, name="register_failure"),
    path("registration/<int:registration_id>/success", views.register_success, name="register_success"),
    path("registration/<int:registration_id>/pay", views.initiate_payment, name="initiate_payment"),
    path("registration/<int:registration_id>/retry", views.retry_payment, name="retry_payment"),
    path("payment/callback", views.payment_callback, name="payment_callback"),
]
