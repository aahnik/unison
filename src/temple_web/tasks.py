from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_email_in_bg(
    subject: str, message: str, recipient_list: list[str], html_message: str
):
    """A wrapper around Django's send_mail to send emails using celery"""
    send_mail(
        subject=subject,
        message=message,
        recipient_list=recipient_list,
        html_message=html_message,
        fail_silently=False,
    )
