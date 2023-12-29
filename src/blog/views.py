from django.shortcuts import render
from django.http import HttpRequest
from .models import BlogPost

import logging

log = logging.getLogger(__name__)


def blog_list(request: HttpRequest):
    blogs = BlogPost.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog/list.html", context=context)


def blog_item(request: HttpRequest, slug: str):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        "blog": blog,
        "author_name": "Aahnik",
        "author_bio": "Nice work",
        "date_pub": "9 Jan",
    }
    return render(request, "blog/item.html", context=context)
