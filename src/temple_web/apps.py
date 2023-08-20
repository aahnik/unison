from django.contrib.admin.apps import AdminConfig


class TempleWebAdminConfig(AdminConfig):
    default_site = "temple_web.admin.TempleWebAdminSite"
