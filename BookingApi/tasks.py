# from time import sleep 
# from django.core.mail import send_mail 
# from celery import shared_task

# @shared_task()
# def send_mail_task(email_address,message, **kwargs):
#     sleep(2)
#     send_mail(
#         print("your ticket booked check email: {email_addreess}",", ",message)
#     )

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_email_ticket_book(subject, message, recipient_list):
    # Send the email
    send_mail(
        subject,
        strip_tags(message),  # Plain text version of the message
        'admin@BookMyShow.com',  # Sender's email address
        recipient_list,  # Recipient's email address or a list of addresses
        html_message=message,  # HTML content of the email
    )

@shared_task
def send_email_event_update(subject, message, recipient_list):
    # Send the email
    send_mail(
        subject,
        strip_tags(message),  # Plain text version of the message
        'admin@BookMyShow.com',  # Sender's email address
        recipient_list,  # Recipient's email address or a list of addresses
        html_message=message,  # HTML content of the email
    )