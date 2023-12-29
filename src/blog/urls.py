from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name="blogs"),
    path("<slug>", views.blog_item, name="blogs"),
]
