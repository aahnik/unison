# Generated by Django 4.2.1 on 2023-07-10 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calltoaction",
            name="fa_icon",
            field=models.CharField(
                default="fa-solid fa-wand-magic-sparkles", max_length=4096
            ),
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "link_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="home.link",
                    ),
                ),
                (
                    "fa_icon",
                    models.CharField(default="fa-brand fa-facebook", max_length=4096),
                ),
                (
                    "site_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.siteconfig",
                    ),
                ),
            ],
            bases=("home.link",),
        ),
    ]