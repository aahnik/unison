# Generated by Django 4.2.1 on 2024-01-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="homecontent",
            name="activity_heading",
            field=models.CharField(default="Activities", max_length=256),
        ),
    ]
