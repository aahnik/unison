from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import (
    FooterLink,
    FooterLinkCateg,
    SiteConfig,
    NavLink,
    CarouselImage,
    GalleryImage,
    CallToAction,
    HomeContent,
    SocialLink,
    FooterAddress,
)


class NavLinkForm(forms.ModelForm):
    class Meta:
        model = NavLink
        fields = ["title", "link"]


class CallToActionForm(forms.ModelForm):
    class Meta:
        model = CallToAction
        fields = ["title", "description", "link", "button_text", "fa_icon"]


class CallToActionInline(admin.StackedInline):
    model = CallToAction
    form = CallToActionForm
    extra = 1
    min_num = 1
    validate_min = True


@admin.register(HomeContent)
class HomeContentAdmin(SingletonModelAdmin):
    inlines = [CallToActionInline]


class NavLinkInline(admin.StackedInline):
    model = NavLink
    form = NavLinkForm
    extra = 0


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 0


class FooterAddressInline(admin.StackedInline):
    model = FooterAddress
    extra = 0
    min_num = 1
    max_num = 1


@admin.register(SiteConfig)
class SiteConfigAdmin(SingletonModelAdmin):
    inlines = [NavLinkInline, SocialLinkInline, FooterAddressInline]


class FooterLinkInline(admin.StackedInline):
    model = FooterLink
    extra = 1


@admin.register(FooterLinkCateg)
class FooterLinkCategAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline]


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ["id", "alt_text", "image", "redirect_url"]


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["id", "alt_text", "image", "redirect_url"]
