from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("get-statement", views.get_statement, name="get-statement"),
    path("invoice", views.view_invoice, name="view-invoice"),
]
