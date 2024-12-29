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
    search_fields = ["event__name", "user__email", "order_id", "client_txn_id"]
    list_display = [
        "registration_number",
        "event",
        "user_name",
        "user_whatsapp",
        "datetime",
        "amount",
        "payment_status",
        "order_id",
        "payment_date_time",
    ]
    list_filter = ["event__name", "payment_status"]
    readonly_fields = [
        "datetime",
        "form_responses",
        "payment_status",
        "order_id",
        "client_txn_id",
        "payment_date_time",
        "payment_data",
        "get_payment_details"
    ]

    fieldsets = [
        (None, {
            'fields': [
                "event",
                "user",
                "datetime",
                "amount",
                "form_responses",
            ]
        }),
        ('Payment Information', {
            'fields': [
                "payment_status",
                "order_id",
                "client_txn_id",
                "payment_date_time",
            ],
            'classes': ['collapse']
        }),
        ('Payment Diagnostic Data', {
            'fields': [
                "get_payment_details",
            ],
            'classes': ['collapse'],
            'description': 'Detailed payment transaction data from UPI gateway'
        })
    ]

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('event', 'user')

    def registration_number(self, obj):
        return obj.registration_number
    registration_number.short_description = "Registration No."

    def get_payment_details(self, obj):
        if not obj.payment_data:
            return "No payment data available"

        # Format payment data for display
        details = []
        if obj.payment_data.get('customer_vpa'):
            details.append(f"Customer UPI: {obj.payment_data['customer_vpa']}")
        if obj.payment_data.get('upi_txn_id'):
            details.append(f"UPI Transaction ID: {obj.payment_data['upi_txn_id']}")
        if obj.payment_data.get('status'):
            details.append(f"Status: {obj.payment_data['status']}")
        if obj.payment_data.get('remark'):
            details.append(f"Remark: {obj.payment_data['remark']}")
        if obj.payment_data.get('txnAt'):
            details.append(f"Transaction Time: {obj.payment_data['txnAt']}")

        # Merchant details
        merchant = obj.payment_data.get('merchant', {})
        if merchant:
            details.append("Merchant Details:")
            if merchant.get('name'):
                details.append(f"  - Name: {merchant['name']}")
            if merchant.get('upi_id'):
                details.append(f"  - UPI ID: {merchant['upi_id']}")

        # User defined fields
        for i in range(1, 4):
            udf = obj.payment_data.get(f'udf{i}')
            if udf:
                details.append(f"UDF{i}: {udf}")

        if obj.payment_data.get('createdAt'):
            details.append(f"Created At: {obj.payment_data['createdAt']}")

        return "\n".join(details)
    get_payment_details.short_description = "Payment Details"
