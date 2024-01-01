from django.shortcuts import render
from django.http import HttpRequest
from .models import CommunityActivity

import logging

log = logging.getLogger(__name__)


def activities_item(request: HttpRequest, slug: str):
    ac = CommunityActivity.objects.get(slug=slug)
    context = {"ac": ac}
    return render(request, "activities/item.html", context=context)
