from django.db import models
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


# Create your models here.


class NavLink(models.Model):
    home_config = models.ForeignKey("HomeConfig", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        if NavLink.objects.count() >= 7:
            raise ValidationError("Maximum number of instances of NavLink reached.")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title




class HomeConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default="Site Name")
    maintenance_mode = models.BooleanField(default=False)
    map_embed_url = models.CharField(max_length=5000, default="helllo")

    def __str__(self):
        return self.site_name + " Config"


class HomeCarousel(models.Model):
    pass


class HomeGallery(models.Model):
    pass
