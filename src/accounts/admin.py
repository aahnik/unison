from django.contrib import admin
from .models import (
    ExpenseCategory,
    Transanction,
    FundRaiser,
    PaymentMode,
    BillerDetails,
    # AdminLinkModel
)
from solo.admin import SingletonModelAdmin
# from utils.admin_links import BaseCustomAdmin
# from django.urls import reverse
# from django.shortcuts import redirect



@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ["category", "category_balance"]
    pass


@admin.register(FundRaiser)
class FundraiserAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):
    pass


@admin.register(BillerDetails)
class BillerDetailsAdmin(SingletonModelAdmin):
    pass


class AmountRangeFilter(admin.SimpleListFilter):
    title = "Amount Range"
    parameter_name = "amount_range"

    def lookups(self, request, model_admin):
        return (
            ("0-1000", "0 - 1000"),
            ("1000-5000", "1000 - 5000"),
            ("5000-10000", "5000 - 10000"),
            ("10000", "10000 and above"),
        )

    def queryset(self, request, queryset):
        if self.value() == "0-1000":
            return queryset.filter(amount__range=(0, 1000))
        elif self.value() == "1000-5000":
            return queryset.filter(amount__range=(1000, 5000))
        elif self.value() == "5000-10000":
            return queryset.filter(amount__range=(5000, 10000))
        elif self.value() == "10000":
            return queryset.filter(amount__gte=10000)


@admin.register(Transanction)
class TransanctionAdmin(admin.ModelAdmin):
    search_fields = ["amount", "purpose"]
    list_display = [
        "ttype",
        "amount",
        "purpose",
        "txn_status",
        "mode",
        "tdate",
        "category",
        "invoice_link",
    ]
    list_filter = [
        "ttype",
        "category",
        "txn_status",
        "fund_raiser",
        AmountRangeFilter,
        "tdate",
        "mode",
    ]

# @admin.register(AdminLinkModel)
# class GetStatementViewLinkAdmin(BaseCustomAdmin):
#     def custom_view(self, request):
#         return redirect(reverse("accounts:get-statement"))
