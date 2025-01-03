# Generated by Django 4.2.1 on 2024-12-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("haps", "0005_event_login_required_event_registration_fee_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventregistration",
            name="client_txn_id",
            field=models.CharField(
                blank=True, db_index=True, max_length=128, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="eventregistration",
            name="payment_data",
            field=models.JSONField(
                default=dict,
                help_text="\n    Stores payment-related data from UPI gateway including:\n    - customer_vpa: Customer's UPI ID\n    - upi_txn_id: UPI transaction ID\n    - status: Detailed payment status\n    - remark: Payment remarks/failure reason\n    - txnAt: Transaction timestamp\n    - merchant: Merchant details (name, upi_id)\n    - udf1, udf2, udf3: User defined fields\n    - redirect_url: Payment redirect URL\n    - createdAt: Order creation time\n    ",
            ),
        ),
        migrations.AddField(
            model_name="eventregistration",
            name="payment_date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
