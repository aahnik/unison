from django.contrib import admin
from .models import EventRegistration, Event, EventFormField


class EventFormFieldInline(admin.TabularInline):
    model = EventFormField
    extra = 1
    ordering = ['order']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
        "venue",
        "start_time",
        "accept_reg",
        "show_on_home",
        "login_required",
        "registration_fee",
        "event_page",
    ]
    list_filter = ["show_on_home", "accept_reg", "login_required"]
    fieldsets = [
        (None, {
            'fields': [
                "name",
                "description",
                "cover_image",
                "venue",
                "start_time",
                "end_time",
            ]
        }),
        ('Registration Settings', {
            'fields': [
                "accept_reg",
                "login_required",
                "registration_fee",
            ],
            'description': 'Configure how users can register for this event'
        }),
        ('Display Settings', {
            'fields': [
                "show_on_home",
                "content",
            ]
        })
    ]
    inlines = [EventFormFieldInline]


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    search_fields = ["event__name", "user__email", "order_id"]
    list_display = [
        "event",
        "user_name",
        "user_whatsapp",
        "datetime",
        "amount",
        "payment_status",
        "order_id"
    ]
    list_filter = ["event__name", "payment_status"]
    readonly_fields = ["datetime", "form_responses"]

    def has_add_permission(self, request):
        return False  # Registrations should only be created through the website

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('event', 'user')
