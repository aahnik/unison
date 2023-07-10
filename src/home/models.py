from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel
from utils.images import upload_image_to, extract_timestamp
from urllib.parse import urlparse
from consts.validators import FA_ICON_BRANDS_ALLOWED

# Create your models here.


class ModelImage(models.Model):
    alt_text = models.CharField(max_length=512, default="image")
    redirect_url = models.CharField(max_length=512, blank=True, null=True, default="")
    image = models.ImageField(upload_to=upload_image_to)

    class Meta:
        abstract = True

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

    class Meta:
        abstract = True
    def __str__(self) -> str:
        return self.title


class CarouselImage(ModelImage):
    pass


class GalleryImage(ModelImage):
    pass


class NavLink(Link):
    site_config = models.ForeignKey("SiteConfig", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if NavLink.objects.count() >= 7:
            raise ValidationError("Maximum number of instances of NavLink reached.")
        super().save(*args, **kwargs)


class SocialLink(Link):
    site_config = models.ForeignKey("SiteConfig", on_delete=models.CASCADE)
    icon_brand = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        try:
            icon_brand = urlparse(self.link).netloc.split(".")[-2]
            assert icon_brand in FA_ICON_BRANDS_ALLOWED, "Unknown brand"
            self.icon_brand = f"fa-brands fa-{icon_brand}"

        except Exception as _:
            self.icon_brand = "fa-solid fa-link"
        super().save(args, kwargs)


class FooterLinkCateg(models.Model):
    site_config = models.ForeignKey("SiteConfig", on_delete=models.CASCADE)
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
    fa_icon = models.CharField(
        max_length=4096, default="fa-solid fa-wand-magic-sparkles"
    )


NEWSLETTER_ICON_CHOICES = [
    ("fa-brands fa-whatsapp", "Whatsapp"),
    ("fa-regular fa-envelope", "Email"),
]


class HomeContent(SingletonModel):
    map_embed_url = models.CharField(max_length=5000)
    newsletter_signup_header = models.CharField(
        max_length=256, default="Sign up for newsletter"
    )
    newsletter_signup_subtitle = models.TextField(
        max_length=2048,
        default="Stay up to date with the roadmap progress, announcements and exclusive discounts feel free to sign up with your email.",
    )
    newsletter_signup_placeholder = models.CharField(
        max_length=256, default="Enter your email"
    )
    newsletter_icon = models.CharField(
        max_length=100,
        choices=NEWSLETTER_ICON_CHOICES,
        default=NEWSLETTER_ICON_CHOICES[1][0],
    )


class SiteConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default="Temple Web")
    maintenance_mode = models.BooleanField(default=False)
    # seperate out map embed url from home config
    # home config is shared across all templates via context processors
    favicon = models.ImageField(upload_to=upload_image_to, null=True, blank=True)
    logo = models.ImageField(upload_to=upload_image_to, null=True, blank=True)

    def __str__(self):
        return self.site_name + " Config"
