from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel
from utils.images import upload_image_to, extract_timestamp

# Create your models here.


class ModelImage(models.Model):
    alt_text = models.CharField(max_length=512)
    redirect_url = models.CharField(max_length=512, blank=True, null=True, default="")
    image = models.ImageField(upload_to=upload_image_to)

    def __str__(self):
        return self.alt_text

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        # print(self.redirect_url)
        if self.redirect_url is None or (
            extract_timestamp(self.redirect_url) is not None
            and extract_timestamp(self.redirect_url)
            != extract_timestamp(self.image.url)
        ):
            self.redirect_url = self.image.url
            print(self.redirect_url)

        super().save(args, kwargs)


class Link(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=1024, default="")

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


class CallToAction(models.Model):
    # cta sections in home page
    home_content = models.ForeignKey("HomeContent", on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default="Call to Action Card")
    description = models.CharField(max_length=1024)
    button_text = models.CharField(max_length=32)
    fa_icon_html = models.CharField(max_length=4096)


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
