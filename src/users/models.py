from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.images import upload_image_to

from .managers import TempleWebUserManager


class TempleWebUser(AbstractUser):
    username = None
    email = models.EmailField("email address", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = TempleWebUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(TempleWebUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=upload_image_to)
    address = models.TextField(max_length=1024)
    profession = models.CharField(max_length=256)
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.__str__()
