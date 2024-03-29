# Generated by Django 4.2.1 on 2023-12-16 06:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DonationConfig",
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
                ("title", models.CharField(max_length=1024)),
                ("subtitle", models.CharField(max_length=4096)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DonationTier",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.CharField(max_length=1024)),
                (
                    "amount",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(10000)]
                    ),
                ),
                ("visible", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="TierFeature",
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
                ("feature", models.CharField(max_length=512)),
                (
                    "donation_tier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="donations.donationtier",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonationReceived",
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
                ("name", models.CharField(max_length=512)),
                ("whatsapp_number", models.CharField(max_length=12)),
                ("occupation", models.CharField(max_length=512)),
                (
                    "amount",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(10000)]
                    ),
                ),
                ("address", models.TextField(max_length=4096)),
                ("payment_date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("success", "Success"),
                            ("failure", "Failure"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("order_id", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "client_txn_id",
                    models.CharField(db_index=True, max_length=128, unique=True),
                ),
                (
                    "customer_vpa",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("remark", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "upi_transaction_id",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "merchant_name",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "merchant_upi_id",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "donation_tier",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="donations.donationtier",
                    ),
                ),
            ],
        ),
    ]
