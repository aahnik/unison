from django.contrib import admin
from .models import CommunityActivity
# Register your models here.

@admin.register(CommunityActivity)
class CommunityActivityAdmin(admin.ModelAdmin):
    pass
