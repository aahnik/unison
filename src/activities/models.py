from django.db import models
from utils.images import upload_image_to

# Create your models here.


class CommunityActivity(models.Model):
    title = models.CharField(max_length=512, default="Group Study")
    summary = models.CharField(max_length=1024, default="Activity description in short")

    description = models.TextField(
        max_length=10240, default="Detailed activity description"
    )
    fa_icon = models.TextField(max_length=100, default="fa-solid fa-graduation-cap")
    cover_image = models.ImageField(upload_to=upload_image_to, null=True, blank=True)

    def __str__(self):
        return self.title
