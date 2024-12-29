from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from utils.images import upload_image_to
from utils.slugs import generate_unique_slug
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserProfile

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=4096)
    cover_image = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    venue = models.CharField(max_length=128)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
    accept_reg = models.BooleanField(verbose_name="Accepting registrations ?")
    show_on_home = models.BooleanField(verbose_name="Show on Home Page ?")
    content = RichTextUploadingField(null=True, blank=True)
    login_required = models.BooleanField(default=True, verbose_name="Login required for registration?")
    registration_fee = models.PositiveIntegerField(null=True, blank=True, help_text="Leave blank for free registration")

    def __str__(self):
        return self.name + "  (" + str(self.start_time) + ")"

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = generate_unique_slug(self.name, Event)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/events/{self.slug}"

    def event_page(self):
        return format_html(
            f'<a href="{self.get_absolute_url()}" target="_blank">View Page</a>'
        )


class EventFormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text Input'),
        ('number', 'Number Input'),
        ('email', 'Email Input'),
        ('textarea', 'Text Area'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='form_fields')
    field_label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    help_text = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order']
        unique_together = ['event', 'field_label']

    def __str__(self):
        return f"{self.event.name} - {self.field_label}"


class EventRegistration(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failure', 'Failure'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    form_responses = models.JSONField(default=dict)
    amount = models.PositiveIntegerField(null=True, blank=True)

    # Payment related fields
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )
    order_id = models.CharField(max_length=100, blank=True, null=True)
    client_txn_id = models.CharField(max_length=128, unique=True, db_index=True, null=True, blank=True)
    payment_date_time = models.DateTimeField(null=True, blank=True)

    # Payment diagnostic data from UPI gateway
    payment_data = models.JSONField(default=dict, help_text="""
    Stores payment-related data from UPI gateway including:
    - customer_vpa: Customer's UPI ID
    - upi_txn_id: UPI transaction ID
    - status: Detailed payment status
    - remark: Payment remarks/failure reason
    - txnAt: Transaction timestamp
    - merchant: Merchant details (name, upi_id)
    - udf1, udf2, udf3: User defined fields
    - redirect_url: Payment redirect URL
    - createdAt: Order creation time
    """)

    def __str__(self):
        return f"Registration #{self.id} - {self.event.name}"

    @property
    def registration_number(self):
        """Returns a formatted registration number."""
        return f"#{self.id}"


    def user_name(self):
        if self.user:
            return self.user.full_name()
        return self.form_responses.get('name', 'Anonymous')

    def user_whatsapp(self):
        if self.user:
            return UserProfile.objects.get(user=self.user).whatsapp_number
        return self.form_responses.get('whatsapp_number', '')

    def user_profile_link(self):
        if self.user:
            return self.user.profile_link()
        return None

    def __str__(self) -> str:
        user_str = str(self.user) if self.user else self.form_responses.get('name', 'Anonymous')
        return f"{user_str} % {self.event}"