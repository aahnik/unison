# Generated by Django 4.2.1 on 2024-01-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "activities",
            "0002_communityactivity_content_communityactivity_slug_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="communityactivity",
            name="title",
            field=models.CharField(default="Activity Name", max_length=512),
        ),
    ]