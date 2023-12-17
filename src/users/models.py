from django.contrib.auth.models import AbstractUser
from django.db import models


from .managers import TempleWebUserManager


class TempleWebUser(AbstractUser):
    username = None
    email = models.EmailField("email address", max_length=255, unique=True)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = TempleWebUserManager()

    def __str__(self):
        return self.email

# class UserProfile(models.Model):
#     user = models.OneToOneField(TempleWebUser, on_delete=)
