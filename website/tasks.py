from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_contact_email_task(name, email, subject, message):
    """
    Sends an email to the admin asynchronously via Celery.
    """
    email_body = f"Message from: {name} <{email}>\n\nSubject: {subject}\n\nMessage:\n{message}"
    
    try:
        send_mail(
            subject=f"New Portfolio Contact: {subject}",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Assuming sending to self
            fail_silently=False,
        )
        logger.info(f"Successfully sent contact email from {name}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email from {name}: {str(e)}")
        # You could also raise the exception for celery to retry
        return False
