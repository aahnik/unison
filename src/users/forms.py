from django import forms
from .models import TempleWebUser, UserProfile
from django.core.exceptions import ValidationError


class TempleWebUserCreationForm(forms.ModelForm):
    """A form for creating new users from the admin"""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = TempleWebUser
        fields = ["email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=1024)
    profession = forms.CharField(max_length=256)
    whatsapp_number = forms.CharField(max_length=15)
    email = forms.CharField(max_length=128)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_pic", "address", "profession", "whatsapp_number"]
