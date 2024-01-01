from django.db import models
from utils.images import upload_image_to
from ckeditor_uploader.fields import RichTextUploadingField
from utils.slugs import generate_unique_slug
from django.utils.html import format_html


class CommunityActivity(models.Model):
    title = models.CharField(max_length=512, default="Activity Name")
    summary = models.CharField(max_length=1024, default="Activity description in short")
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(
        max_length=1024, default="Detailed activity description"
    )
    fa_icon = models.TextField(max_length=100, default="fa-solid fa-graduation-cap")
    cover_image = models.ImageField(upload_to=upload_image_to, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = generate_unique_slug(self.title, CommunityActivity)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return f"/activity/{self.slug}"

    def activity_page(self):
        return format_html(
            f'<a href="{self.get_absolute_url()}" target="_blank">View Page</a>'
        )
