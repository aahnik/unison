from django.contrib import admin
from .models import EventRegistration, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
        "venue",
        "start_time",
        "accept_reg",
        "show_on_home",
        "event_page",
    ]
    list_filter = ["show_on_home", "accept_reg"]
    fields = [
        "name",
        "description",
        "cover_image",
        "venue",
        "start_time",
        "end_time",
        "accept_reg",
        "show_on_home",
    ]


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    search_fields = ["event", "user"]
    list_display = ["user", "event"]
    list_filter = ["event__name"]
