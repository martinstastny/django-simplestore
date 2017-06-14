from __future__ import absolute_import
from celery import task
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

@task(name="send_order_confirmation", max_retries=3, soft_time_limit=5)
def send_email_confirmation(data):
    """
    Send email with order details
    """
    message = get_template("emails/order_conf.html").render(Context(data))
    mail = EmailMessage(
        subject="Order confirmation",
        body=message,
        from_email='test@martinstastny.cz',
        to=['me@martinstastny.cz'],
        reply_to=['test@martinstastny.cz'],
    )
    mail.content_subtype = "html"
    return mail.send()
