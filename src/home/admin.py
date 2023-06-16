from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import FooterLink, FooterLinkCateg, HomeConfig, Image, NavLink


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


class FooterLinkInline(admin.StackedInline):
    model = FooterLink
    extra = 1


@admin.register(FooterLinkCateg)
class FooterLinkCategAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline]


# @admin.register(FooterLink)
# class FooterLinkAdmin(admin.ModelAdmin):
#     pass
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "test_image"]
