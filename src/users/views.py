from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model

from .models import TempleWebUser, UserProfile
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from utils.adirect import adirect

User = get_user_model()


def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("users:me_view")
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_view = request.GET.get("next", "users:me_view")
                return redirect(next_view)
                # NOTE:
                # name of the view needs to be as defined in urls.py urlpatters,
                # and not the function name
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
def me_view(request: HttpRequest, edit: str = "view"):
    user_profile, truth = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("users:me_view")
    else:
        # user_profile, truth = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=user_profile)
    return render(
        request,
        "users/profile.html",
        {"form": form, "user": request.user, "user_profile": user_profile},
    )


def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("users:me_view")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = User.objects.create_user(email, password)
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()

            user_profile = UserProfile(
                user=user,
                address=form.cleaned_data["address"],
                profession=form.cleaned_data["profession"],
                whatsapp_number=form.cleaned_data["whatsapp_number"],
            )
            user_profile.save()

            login(request, user)
            next_view = request.GET.get("next", "users:me_view")
            return redirect(next_view)
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def forgot_password(request: HttpRequest):
    pass


@permission_required("is_superuser", login_url="/users/login")
def user_profile(request: HttpRequest, email: str):
    user = User.objects.get(email=email)
    user_profile, t = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("users:profile", email=email)
    else:
        form = UserProfileForm(instance=user_profile)
    return render(
        request,
        "users/profile.html",
        {"form": form, "user": user, "user_profile": user_profile},
    )
