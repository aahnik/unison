import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "temple_web.settings")
app = Celery("temple_web")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
