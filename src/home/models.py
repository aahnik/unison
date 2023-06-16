import os
from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel

# Create your models here.



def upload_to(instance, filename):
    # Get the file extension
    ext = os.path.splitext(filename)[1]
    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Create the filename with the timestamp
    new_filename = f"{timestamp}{ext}"
    # Return the path relative to MEDIA_ROOT
    return os.path.join("images", new_filename)


class Link(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=1024, default="/")

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    test_image = models.ImageField(upload_to=upload_to)


class NavLink(Link):
    home_config = models.ForeignKey("HomeConfig", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if NavLink.objects.count() >= 7:
            raise ValidationError("Maximum number of instances of NavLink reached.")
        super().save(*args, **kwargs)


class FooterLinkCateg(models.Model):
    home_config = models.ForeignKey("HomeConfig", on_delete=models.CASCADE)
    categ_title = models.CharField(max_length=100)

    def __str__(self):
        return self.categ_title


class FooterLink(Link):
    footer_link_categ = models.ForeignKey("FooterLinkCateg", on_delete=models.CASCADE)


class HomeConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default="Temple Web")
    maintenance_mode = models.BooleanField(default=False)
    map_embed_url = models.CharField(max_length=5000, default="helllo")

    def __str__(self):
        return self.site_name + " Config"


class HomeCarousel(models.Model):
    pass


class HomeGallery(models.Model):
    pass
