from django.http import HttpResponse
from django.shortcuts import render

from .models import HomeConfig, NavLink


def index(request):
    home_config = HomeConfig.objects.get()
    nav_links = NavLink.objects.all()

    context = {
        "home_config": home_config,
        "nav_links": nav_links
    }
    return render(request, "home/index.html", context=context)
