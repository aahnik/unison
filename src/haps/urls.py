from django.urls import path

from . import views

app_name = "haps"

urlpatterns = [
    path("", views.haps_list, name="events"),
    path("<slug>", views.haps_item, name="event_item"),
]
