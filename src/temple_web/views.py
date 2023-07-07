from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpRequest


def page_not_found_view(request: HttpRequest, exception):
    # print("hello", request.get_full_path())
    return render(request, "404.html", {}, status=404)
