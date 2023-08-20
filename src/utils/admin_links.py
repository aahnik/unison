from django.contrib import admin
from django.shortcuts import redirect

# copy paste this base class to your models.py

# class AdminLinkModel(models.Model):
#     # a blank dummy model for registering links in admin page
#     # create a child class in models.py and set proxy=True inside class Meta
#     pass


class ViewLinkAdmin(admin.ModelAdmin):
    # create a child class, and define your own redirect link

    redirect_link = "/"

    def changelist_view(self, request, extra_context=None):
        return redirect(self.redirect_link)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
