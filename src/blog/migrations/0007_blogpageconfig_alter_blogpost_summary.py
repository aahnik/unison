# Generated by Django 4.2.1 on 2024-01-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_blogpost_cover_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPageConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Our Blog", max_length=1024)),
                (
                    "subtitle",
                    models.TextField(default="Here lives our blog", max_length=4096),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="summary",
            field=models.TextField(max_length=1024),
        ),
    ]