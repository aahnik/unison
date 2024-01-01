from django.contrib import admin
from .models import CommunityActivity
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.


class CommunityActivityAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = CommunityActivity
        exclude = ["slug", "fa_icon"]


@admin.register(CommunityActivity)
class CommunityActivityAdmin(admin.ModelAdmin):
    form = CommunityActivityAdminForm
    list_display = ["title", "activity_page"]
