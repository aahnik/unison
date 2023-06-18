from django.http import HttpResponse
from django.shortcuts import render

from .models import FooterLinkCateg, HomeConfig, NavLink


def index(request):
    # images = Image.objects.all()

    context = {}
    return render(request, "home/index.html", context=context)
