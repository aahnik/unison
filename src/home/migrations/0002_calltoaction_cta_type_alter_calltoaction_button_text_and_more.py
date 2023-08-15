# Generated by Django 4.2.1 on 2023-07-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="calltoaction",
            name="cta_type",
            field=models.CharField(default="Activity", max_length=20),
        ),
        migrations.AlterField(
            model_name="calltoaction",
            name="button_text",
            field=models.CharField(default="Read more", max_length=32),
        ),
        migrations.AlterField(
            model_name="calltoaction",
            name="description",
            field=models.CharField(
                default="Some description of this page.", max_length=1024
            ),
        ),
    ]
