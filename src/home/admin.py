from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import HomeConfig, NavLink

from django import forms


class NavLinkForm(forms.ModelForm):
    class Meta:
        model = NavLink
        fields = ["title", "link"]


class NavLinkInline(admin.StackedInline):
    model = NavLink
    form = NavLinkForm
    extra = 1
    min_num = 1
    validate_min = True


@admin.register(HomeConfig)
class HomeConfigAdmin(SingletonModelAdmin):
    inlines = [NavLinkInline]
