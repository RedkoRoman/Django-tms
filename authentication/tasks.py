from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@shared_task
def send_activation_email_task(email, message):
    sleep(20)
    send_mail(
        subject='Test',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
    logger.info(f'Email send successfully to {email}')