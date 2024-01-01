from django.urls import path

from . import views

app_name = "activities"

urlpatterns = [
    path("<slug>", views.activities_item, name="activities_item"),
]
