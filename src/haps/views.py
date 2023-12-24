from django.shortcuts import render
from django.http import HttpRequest, Http404
from .models import Event
import logging

log = logging.getLogger(__name__)


def haps_list(request: HttpRequest):
    haps = Event.objects.all()
    context = {"haps": haps}
    return render(request, "haps/list.html", context=context)


def haps_item(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    context = {"event": event}

    return render(request, "haps/item.html", context=context)
