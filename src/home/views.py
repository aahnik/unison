from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import FooterLinkCateg, HomeConfig, NavLink


def index(request):
    # images = Image.objects.all()

    context = {}
    return render(request, "home/index.html", context=context)

def dev_test(request):
    raise Http404("Dev testing 404")