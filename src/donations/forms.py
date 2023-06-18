from django import forms
from .models import DonationReceived


class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationReceived
        fields = [
            "name",
            "whatsapp_number",
            "occupation",
            "donation_tier",
            "amount",
            "address",
        ]
