from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import CarouselImage, GalleryImage


def index(request):
    carousel_images = CarouselImage.objects.all()
    gallery_images = GalleryImage.objects.all()

    context = {"carousel_images": carousel_images, "gallery_images": gallery_images}
    return render(request, "home/index.html", context=context)


def dev_test(request):
    raise Http404("Dev testing 404")
