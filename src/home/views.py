from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import CarouselImage, GalleryImage, HomeContent, CallToAction
from activities.models import CommunityActivity
from blog.models import BlogPost
from haps.models import Event


def index(request):
    context = {
        "carousel_images": CarouselImage.objects.all(),
        "gallery_images": GalleryImage.objects.all(),
        "home_content": HomeContent.get_solo(),
        "activities": CommunityActivity.objects.all(),
        "ctas": CallToAction.objects.all(),
        "blogs": BlogPost.objects.order_by("-created_at")[:4],
        "haps": Event.objects.filter(show_on_home=True)[:2],
    }
    return render(request, "home/index.html", context=context)


def dev_test(request):
    raise Http404("Dev testing 404")
