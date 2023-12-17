from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate

from .models import TempleWebUser
from .forms import TempleWebUserCreationForm, UserLoginForm

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("users:me_view")
                # NOTE: name of the view needs to be as defined in urls.py urlpatters, and not the function name
            else:
                form.add_error(
                    None, ValidationError("Incorrect username or password")
                )  # this is a non field error
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return render(request, "users/logout.html")


@login_required(login_url="/users/login")
def me_view(request: HttpRequest):
    return render(request, "users/profile.html", {"email": request.user.email})


def register(request: HttpRequest):
    if request.method == "POST":
        form = TempleWebUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:me_view")
    else:
        form = TempleWebUserCreationForm()

    return render(request, "users/register.html", {"form": form})
