from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name="blogs_list"),
    path("<slug>", views.blog_item, name="blog_item"),
]
