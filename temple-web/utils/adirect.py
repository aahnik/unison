# adirect is aahnik's redirect

# utility over Django's redirect
from django.shortcuts import redirect
from django.urls import reverse

from urllib.parse import urlencode


def adirect(view, **kwargs):
    # view must be the string of the view
    query_params = urlencode(kwargs, doseq=True)
    return redirect(reverse(view) + "?" + query_params)
