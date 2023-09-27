from rest_framework import serializers
from .models import User,EventOrganizer,Customer,Event,Tickets,Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('is_customer','is_eventOrganizer')


class EventOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrganizer
        fields = ('user_ev','name','age','email')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user_cu','name','age','phone_number')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id','evOrg','date','title','venue')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('ticket_id','evOrg','ticket_type','is_event','price','ticket_available','ticket_booked')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id','cust','event','ticket_id','time')
