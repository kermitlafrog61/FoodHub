import os

from celery import Celery
from django.core.mail import send_mail
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def send_test_email(self):
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
