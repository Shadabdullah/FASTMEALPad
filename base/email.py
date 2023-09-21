# utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_order_confirmation_email(order_id, user_email):
    subject = 'New Order'
    message = f'You have recieved a New Order From {order_id}.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user_email]

    send_mail(subject, message, from_email, to_email)
