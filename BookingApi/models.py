from time import sleep 
from django.core.mail import send_mail 
from celery import shared_task
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
from django.dispatch import receiver
import uuid

# Create your models here.
#here we will make our customer model

def generate_event_id():
    return str(uuid.uuid4()).split("-")[-1]

class User(AbstractUser):
    # is_customer = models.BooleanField(default=False)
    is_eventOrganizer = models.BooleanField(default=False)

class EventOrganizer(models.Model):
    user_ev = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="event_user")
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.EmailField(max_length=200,unique=True)

class Customer(models.Model):
    user_cu = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="customer_user")
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

class Event(models.Model):
    event_id = models.CharField(max_length=50,primary_key=True)
    evOrg = models.ForeignKey(EventOrganizer,on_delete=models.CASCADE,related_name='events')
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=300)

    def __str__(self) -> str:
        return "{} - {}".format(self.title,self.event_id)
    def save(self,*args,**kwargs):
        if len(self.event_id.strip(" ")) == 0 :
            self.event_id = generate_event_id()
        
        super(Event,self).save(*args,**kwargs)

TICKET_TYPE = (
    ('gen_adm','General Admission Ticket'),
    ('luxury','VIP'),
    ('group_pack','Group Package Ticket'),
    ('reserved','Reserved'),
    ('hidden','Hidden'),
    ('virt','Virtual'),
)

class Tickets(models.Model):
    ticket_id = models.CharField(max_length=100,primary_key=True)
    evOrg = models.ForeignKey(EventOrganizer,on_delete=models.CASCADE,related_name='tickets')
    is_event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="which_tickets")
    ticket_type = models.CharField(max_length=50,choices=TICKET_TYPE,default='gen_adm')
    price = models.CharField(max_length=50)
    ticket_available = models.IntegerField()
    ticket_booked = models.IntegerField()

    def bookShow(self):
        self.ticket_available -= 1
        self.ticket_booked += 1 
        self.save()

    def cancelShow(self):
        self.ticket_available += 1 
        self.ticket_booked -= 1 
        self.save()

# @receiver(post_save, sender=Tickets)
# def post_save_ticket(sender, instance, **kwargs):
#     # Check if the ticket is being booked (ticket_available decreased)
#     if instance.ticket_available < instance.ticket_available + 1:
#         instance.bookShow()
#     # Check if the ticket is being canceled (ticket_booked decreased)
#     elif instance.ticket_booked < instance.ticket_booked + 1:
#         instance.cancelShow()
from django.db.models.signals import post_save,post_delete
class Booking(models.Model):
    booking_id = models.CharField(max_length=200,primary_key=True)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='bookings')
    event = models.CharField(max_length=100)
    ticket_id = models.ForeignKey(Tickets,on_delete=models.CASCADE,related_name='booking_ref')
    time = models.DateTimeField(default=timezone.now)
 
    def post_save_ticket(sender, instance, **kwargs):
        # breakpoint()
        instance.ticket_id.bookShow()
        # print("email has been sent to {instance.cust.email}")
    def post_delete_ticket(sender, instance, **kwargs):
        instance.ticket_id.cancelShow()
        
    # @shared_task
    # def send_mail_task(email_address,message, **kwargs):
    #     sleep(2)
    #     # send_mail(
    #     #     "your booked ticket",
    #     #     f"\t{message}\n\nThank you!",
    #     #     "akash.mittal@bonamisoftware.com",
    #     #     [email_address],
    #     #     fail_silently=False,
    #     # )
        
    #     print("sent mail to {email_address}")
    

post_save.connect(Booking.post_save_ticket,sender=Booking)
post_delete.connect(Booking.post_delete_ticket,sender=Booking)
# post_save.connect(Booking.send_mail_task,sender=Booking)

    

    