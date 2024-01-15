from django.shortcuts import render
from django.http import HttpRequest, Http404
from .models import Event, EventRegistration
from django.contrib.auth.decorators import login_required
import logging


log = logging.getLogger(__name__)


def haps_list(request: HttpRequest):
    haps = Event.objects.all()
    context = {"haps": haps}
    return render(request, "haps/list.html", context=context)


def haps_item(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    context = {"hap": event}

    return render(request, "haps/item.html", context=context)


@login_required(login_url="/users/register")
def register_for_event(request: HttpRequest, slug: str):
    event = Event.objects.get(slug=slug)
    registration = EventRegistration.objects.get_or_create(
        event=event, user=request.user
    )

    context = {"event": event, "user": request.user, "reg": registration}
    return render(request, "haps/register_success.html", context=context)
