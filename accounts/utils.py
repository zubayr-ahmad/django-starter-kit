import os
from django.core.mail import EmailMessage
from django.conf import settings


def send_email(data: dict):
    """
    data keys: subject, body, to_email (string or list)
    """
    to = data.get("to_email")
    if isinstance(to, str):
        to = [to]
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", os.environ.get("EMAIL_USER"))
    email = EmailMessage(subject=data.get("subject"), body=data.get("body"),
                            from_email=from_email, to=to)
    email.send(fail_silently=False)
