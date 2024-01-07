from django.contrib import admin
from .models import TempleWebUser
from django.contrib.auth.admin import UserAdmin
from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import TempleWebUserCreationForm


class TempleWebAdminUserChangeForm(forms.ModelForm):
    """A form for updating users from the admin panel"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = TempleWebUser
        fields = [
            "first_name",
            "last_name",
            "is_staff",
            "email",
            "password",
            "is_superuser",
        ]


class TempleWebUserAdmin(UserAdmin):
    form = TempleWebAdminUserChangeForm
    add_form = TempleWebUserCreationForm

    list_display = ["full_name", "email", "date_joined", "is_staff", "profile_link"]
    list_display_links = ["full_name", "email"]
    list_filter = ["is_staff"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                ]
            },
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "groups", "user_permissions"]},
        ),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2", "is_staff"],
            },
        )
    ]

    search_fields = ["email"]
    ordering = ["email"]


# Register your models here.
admin.site.register(TempleWebUser, TempleWebUserAdmin)
