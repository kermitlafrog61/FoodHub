from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_test_email():
    subject = 'Test email'
    message = 'This is a test email'
    recipient_list = ['islam.alybaev61@gmail.com']

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False
    )
