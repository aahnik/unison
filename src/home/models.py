from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel
from utils.images import upload_image_to

# Create your models here.


class ModelImage(models.Model):
    alt_text = models.CharField(max_length=512)
    redirect_url = models.URLField()
    image = models.ImageField(upload_to=upload_image_to)

    def __str__(self):
        return self.alt_text


class Link(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=1024, default="/")

    def __str__(self) -> str:
        return self.title


class CarouselImage(ModelImage):
    pass


class GalleryImage(ModelImage):
    pass


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


class HomeContent(SingletonModel):
    map_embed_url = models.CharField(max_length=5000, default="helllo")


class HomeConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default="Temple Web")
    maintenance_mode = models.BooleanField(default=False)
    # seperate out map embed url from home config
    # home config is shared across all templates via context processors
    favicon = models.ImageField(upload_to=upload_image_to)
    logo = models.ImageField(upload_to=upload_image_to)

    def __str__(self):
        return self.site_name + " Config"
