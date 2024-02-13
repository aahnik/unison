from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import CarouselImage, GalleryImage, HomeContent, CallToAction
from activities.models import CommunityActivity
from blog.models import BlogPost
from haps.models import Event


def index(request):
    home_content = HomeContent.get_solo()
    context = {
        "carousel_images": CarouselImage.objects.all(),
        "gallery_images": GalleryImage.objects.all(),
        "home_content": home_content,
        "activities": CommunityActivity.objects.all(),
        "ctas": CallToAction.objects.all(),
        "blogs": BlogPost.objects.order_by("-created_at")[: home_content.blog_count],
        "haps": Event.objects.filter(show_on_home=True)[:2],
    }
    return render(request, "home/index.html", context=context)


def dev_test(request):
    raise Http404("Dev testing 404")
