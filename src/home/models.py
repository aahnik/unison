from django.db import models
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


# Create your models here.


class Link(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=1024, default="/")

    def __str__(self) -> str:
        return self.title


class NavLink(Link):
    home_config = models.ForeignKey("HomeConfig", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if NavLink.objects.count() >= 7:
            raise ValidationError("Maximum number of instances of NavLink reached.")
        super().save(*args, **kwargs)


class FooterLinkCateg(models.Model):
    home_config = models.ForeignKey("HomeConfig", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class FooterLink(Link):
    footer_link_categ = models.ForeignKey(
        "FooterLinkCateg", on_delete=models.CASCADE
    )


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
