from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def mail_reset_password(user, token):
    """Send a reset password email to the user."""
    context = {"token": token, "name": user.name}
    html_message = render_to_string("mail_reset_password.html", context=context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject="Reset your password",
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
    )
