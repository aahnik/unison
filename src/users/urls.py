from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path("me/", views.me_view, name="me_view"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]

