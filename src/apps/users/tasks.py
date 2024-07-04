from celery import shared_task

from .email import ActivationEmail

@shared_task
def send_activation_email(context, to):
    ActivationEmail(context=context).send(to)

# TODO: create celery beat task to delete old token
