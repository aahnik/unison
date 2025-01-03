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
from django.contrib import admin
from django.urls import include, path
from temple_web import views
from .admin import admin
from . import settings
from . import views

# from django.views.defaults import handler404
handler404 = views.page_not_found_view

urlpatterns = (
    [
        # Health check endpoint
        path('health/', views.health_check, name='health_check'),
        
        path("", include("home.urls")),
        path("donations/", include("donations.urls")),
        # path("online-puja/", include("online_puja.urls")),
        path("activity/", include("activities.urls")),
        path("accounts/", include("accounts.urls")),
        # path("tester/", include("tester.urls")),
        path("users/", include("users.urls")),
        path("events/", include("haps.urls")),
        path("blog/", include("blog.urls")),
        # path("404/", views.page_not_found_view, name="404"),
        path("admin/", admin.site.urls),
        path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
