# Generated by Django 4.2.1 on 2024-01-01 13:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("haps", "0003_eventregistration_datetime"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
