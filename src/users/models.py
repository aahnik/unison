from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.images import upload_image_to
from django.utils.html import format_html
from .managers import TempleWebUserManager
from solo.models import SingletonModel


class TempleWebUser(AbstractUser):
    username = None
    email = models.EmailField("email address", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = TempleWebUserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.get_full_name()

    def profile_link(self):
        return format_html(
            f'<a href="/users/profile/{self.email}" target="_blank">View User Profile</a>'
        )


class UserProfile(models.Model):
    user = models.OneToOneField(TempleWebUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=upload_image_to, null=True, blank=True)
    address = models.TextField(max_length=1024)
    profession = models.CharField(max_length=256)
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.__str__()
