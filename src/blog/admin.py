from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from solo.admin import SingletonModelAdmin

from .models import BlogPost, BlogCategory, BlogPageConfig


@admin.register(BlogPageConfig)
class BlogPageConfigAdmin(SingletonModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        exclude = ["slug", "author"]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    search_fields = ["title", "author"]
    list_display = [
        "title",
        "author",
        "category",
        "created_at",
        "updated_at",
        "blog_page",
    ]
    list_filter = ["category", "created_at", "updated_at"]

    def save_model(self, request, obj, form, change):
        # Set the author field to the user who created the blog
        if not obj.author_id:
            obj.author = request.user
        obj.save()
