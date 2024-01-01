from django.shortcuts import render
from django.http import HttpRequest
from .models import BlogPost, BlogPageConfig

import logging

log = logging.getLogger(__name__)


def blog_list(request: HttpRequest):
    blogs = BlogPost.objects.all()
    blog_config = BlogPageConfig.get_solo()
    context = {"blogs": blogs, "blog_config": blog_config}
    return render(request, "blog/list.html", context=context)


def blog_item(request: HttpRequest, slug: str):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        "blog": blog,
    }
    return render(request, "blog/item.html", context=context)
