from django.contrib import admin
from .models import DonationConfig, DonationTier, TierFeature, DonationReceived
from solo.admin import SingletonModelAdmin

# Register your models here.


@admin.register(DonationConfig)
class DonationConfigAdmin(SingletonModelAdmin):
    pass


class TierFeatureInline(admin.StackedInline):
    model = TierFeature
    extra = 1
    min_num = 1
    max_num = 7


@admin.register(DonationTier)
class DonationTierAdmin(admin.ModelAdmin):
    inlines = [TierFeatureInline]
    list_display = ["name", "amount", "visible"]


@admin.register(DonationReceived)
class DonationReceivedAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "whatsapp_number",
        "donation_tier",
        "amount",
        "payment_date_time",
    ]
