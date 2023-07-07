from django.contrib import admin


class TempleWebAdminSite(admin.AdminSite):
    site_header = "TempleWeb Administration"


admin_site = TempleWebAdminSite(name="TempleWebAdmin")
