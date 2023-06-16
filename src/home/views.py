from django.http import HttpResponse
from django.shortcuts import render

from .models import FooterLinkCateg, HomeConfig, Image, NavLink


def index(request):
    home_config = HomeConfig.get_solo()
    nav_links = NavLink.objects.all()
    footer_categories = FooterLinkCateg.objects.all()
    images = Image.objects.all()

    context = {
        "home_config": home_config,
        "nav_links": nav_links,
        "footer_categories": footer_categories,
        "images": images,
    }
    return render(request, "home/index.html", context=context)
