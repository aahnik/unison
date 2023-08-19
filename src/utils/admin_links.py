# from django.db import models
from django.contrib import admin
from django.urls import path
from django.urls import reverse
from django.shortcuts import redirect


# class AdminLinkModel(models.Model):
#     # blank dummy model
#     class Meta:
#         # abstract = True
#         pass


class BaseCustomAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "custom-view/",
                self.admin_site.admin_view(self.custom_view),
                name="custom-view",
            ),
        ]
        return custom_urls + urls

    def custom_view(self, request):
        # Your custom view logic here
        # this method needs to be overriden  by the children class
        return redirect(reverse("custom-view-url-name"))
