from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from utils.slugs import generate_unique_slug
from django.utils.html import format_html

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = generate_unique_slug(self.title, BlogPost)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def blog_page(self):
        return format_html(
            f'<a href="{self.get_absolute_url()}" target="_blank">View Page</a>'
        )
