from django.db import models
from django.core.validators import MaxValueValidator
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


class DonationConfig(SingletonModel):
    title = models.CharField(max_length=1024)
    subtitle = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class TierFeature(models.Model):
    donation_tier = models.ForeignKey("DonationTier", on_delete=models.CASCADE)
    feature = models.CharField(max_length=512)


class DonationTier(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    amount = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DonationReceived(models.Model):
    name = models.CharField(max_length=512)
    whatsapp_number = models.CharField(max_length=12)
    occupation = models.CharField(max_length=512)
    donation_tier = models.ForeignKey(
        "DonationTier", on_delete=models.SET_NULL, null=True
    )
    amount = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])
    address = models.TextField(max_length=4096)
    payment_date_time = models.DateTimeField(auto_now_add=True)

    PAYMENT_STATUS_CHOICES = ["pending", "success", "failure"]
    payment_status = models.CharField(
        max_length=10,
        choices=[(choice, choice.capitalize()) for choice in PAYMENT_STATUS_CHOICES],
        default="pending",
    )

    def __str__(self):
        return f"{self.name} donated {self.amount} at {str(self.payment_date_time)}"

    def clean(self):
        super().clean()
        donation_tier_amt = DonationTier.objects.get(id=self.donation_tier.pk).amount
        if self.amount < donation_tier_amt:
            raise ValidationError(
                "Donation amount cannot be less than donation tier amount"
            )
