# Generated by Django 4.2.1 on 2023-12-16 06:57

from django.db import migrations, models
import django.db.models.deletion
import utils.images


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarouselImage",
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
                ("alt_text", models.CharField(default="image", max_length=512)),
                (
                    "redirect_url",
                    models.CharField(blank=True, default="", max_length=512, null=True),
                ),
                ("image", models.ImageField(upload_to=utils.images.upload_image_to)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GalleryImage",
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
                ("alt_text", models.CharField(default="image", max_length=512)),
                (
                    "redirect_url",
                    models.CharField(blank=True, default="", max_length=512, null=True),
                ),
                ("image", models.ImageField(upload_to=utils.images.upload_image_to)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HomeContent",
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
                ("map_embed_url", models.CharField(max_length=5000)),
                (
                    "newsletter_signup_header",
                    models.CharField(default="Sign up for newsletter", max_length=256),
                ),
                (
                    "newsletter_signup_subtitle",
                    models.TextField(
                        default="Stay up to date with the roadmap progress, announcements and exclusive discounts feel free to sign up with your email.",
                        max_length=2048,
                    ),
                ),
                (
                    "newsletter_signup_placeholder",
                    models.CharField(default="Enter your email", max_length=256),
                ),
                (
                    "newsletter_icon",
                    models.CharField(
                        choices=[
                            ("fa-brands fa-whatsapp", "Whatsapp"),
                            ("fa-regular fa-envelope", "Email"),
                        ],
                        default="fa-regular fa-envelope",
                        max_length=100,
                    ),
                ),
                (
                    "activity_subhead",
                    models.CharField(
                        default="Here at Temple we focus on overall wellbeing and development.",
                        max_length=512,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SiteConfig",
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
                ("site_name", models.CharField(default="Temple Web", max_length=255)),
                ("maintenance_mode", models.BooleanField(default=False)),
                (
                    "favicon",
                    models.ImageField(
                        blank=True, null=True, upload_to=utils.images.upload_image_to
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to=utils.images.upload_image_to
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SocialLink",
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
                ("title", models.CharField(max_length=256)),
                ("link", models.CharField(default="", max_length=1024)),
                ("icon_brand", models.CharField(blank=True, max_length=50)),
                (
                    "site_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.siteconfig",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NavLink",
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
                ("title", models.CharField(max_length=256)),
                ("link", models.CharField(default="", max_length=1024)),
                (
                    "site_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.siteconfig",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FooterLinkCateg",
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
                ("categ_title", models.CharField(max_length=100)),
                (
                    "site_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.siteconfig",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FooterLink",
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
                ("title", models.CharField(max_length=256)),
                ("link", models.CharField(default="", max_length=1024)),
                (
                    "footer_link_categ",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.footerlinkcateg",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FooterAddress",
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
                (
                    "aline1",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="Address Line 1",
                    ),
                ),
                (
                    "aline2",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="Address Line 2",
                    ),
                ),
                (
                    "aline3",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="Address Line 3",
                    ),
                ),
                (
                    "contact_no",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        verbose_name="Contact Phone no",
                    ),
                ),
                (
                    "site_config",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.siteconfig",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CallToAction",
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
                (
                    "title",
                    models.CharField(default="Call to Action Card", max_length=256),
                ),
                ("cta_type", models.CharField(default="Activity", max_length=20)),
                (
                    "description",
                    models.CharField(
                        default="Some description of this page.", max_length=1024
                    ),
                ),
                ("button_text", models.CharField(default="Read more", max_length=32)),
                ("link", models.CharField(default="/", max_length=256)),
                (
                    "fa_icon",
                    models.CharField(
                        default="fa-solid fa-wand-magic-sparkles", max_length=4096
                    ),
                ),
                (
                    "home_content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.homecontent",
                    ),
                ),
            ],
        ),
    ]
