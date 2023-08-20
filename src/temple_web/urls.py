"""
URL configuration for temple_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import handler404


# from django.contrib import admin
from .admin import admin
from django.urls import include, path
from temple_web import views
from . import settings
from . import views

# from django.views.defaults import handler404
handler404 = views.page_not_found_view

urlpatterns = (
    [
        path("", include("home.urls")),
        path("donations/", include("donations.urls")),
        path("accounts/", include("accounts.urls")),
        # path("404/", views.page_not_found_view, name="404"),
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
