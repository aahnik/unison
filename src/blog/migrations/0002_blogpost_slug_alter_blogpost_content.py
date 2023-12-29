# Generated by Django 4.2.1 on 2023-12-26 20:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]