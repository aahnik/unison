from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from utils.images import upload_image_to
from utils.slugs import generate_unique_slug

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

    def __str__(self):
        return self.name + str(self.start_time)

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = generate_unique_slug(self.name, Event)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return f"/events/{self.slug}"

    def event_page(self):
        return format_html(f'<a href="{self.get_absolute_url()}" target="_blank">View Page</a>')


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.__str__() + "%" + self.event.__str__()
