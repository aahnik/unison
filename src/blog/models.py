from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from utils.slugs import generate_unique_slug
from django.utils.html import format_html
from utils.images import upload_image_to
from solo.models import SingletonModel

User = get_user_model()


class BlogCategory(models.Model):
    label = models.CharField(max_length=32)

    def __str__(self):
        return self.label


class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    category = models.ForeignKey(
        BlogCategory, null=True, blank=True, on_delete=models.SET_NULL
    )
    cover_image = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # if self.author is None:
        #     self.author = self.request.user
        if self.slug == "":
            self.slug = generate_unique_slug(self.title, BlogPost)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def blog_page(self):
        return format_html(
            f'<a href="{self.get_absolute_url()}" target="_blank">View Page</a>'
        )


class BlogPageConfig(SingletonModel):
    title = models.CharField(max_length=1024, default="Our Blog")
    subtitle = models.TextField(max_length=4096, default="Here lives our blog")
