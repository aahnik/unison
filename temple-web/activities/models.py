from django.db import models
from utils.images import upload_image_to
# Create your models here.

class CommunityActivity(models.Model):
    title = models.CharField(max_length=512)
    summary = models.CharField(max_length=1024)
    # icon may be
    description = models.TextField(max_length=10240)
    cover_image = models.ImageField(upload_to=upload_image_to)

    