from django.contrib import admin
from .models import EventOrganizer,Event,Customer,Tickets,Booking,User
# Register your models here.
admin.site.register(User)
admin.site.register(EventOrganizer)
admin.site.register(Event)
admin.site.register(Customer)
admin.site.register(Tickets)
admin.site.register(Booking)





