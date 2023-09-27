from django.shortcuts import render
from .models import Tickets
# from .forms import MyModelForm
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,authentication,permissions
from rest_framework.generics import get_object_or_404
from .serializers import CustomerSerializer,EventOrgSerializer,EventSerializer,TicketSerializer,BookingSerializer,UserSerializer
from .models import Customer,EventOrganizer,Event,Tickets,Booking,User
from BookingApi.tasks import send_email_ticket_book,send_email_event_update
# Create your views here. 

# class UserListView(APIView):
#     def get(self,request):
#         user = User.objects.all()
#         serializer = UserSerializer(user,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request)->Response:
#         # request.data['user_cl'] = request.user.id                                #setting the user as user_cu
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data,status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class UserDetailView(APIView):
#     def get(self,request,pk=None):
#         user = get_object_or_404(Customer.objects.all(),pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self,request,pk=None):
#         user = get_object_or_404(Customer.objects.all(),pk=pk)
#         serializer = UserSerializer(user,data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data)
#     def delete(self,request,pk=None):
#         user = get_object_or_404(User.objects.all(),pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#eventOrganizerAPI
class EventOrganizerListView(APIView):
    def get(self,request):
        ev = EventOrganizer.objects.all()
        serializer = EventOrgSerializer(ev,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        # request.data['user_ev'] = request.user.id    
        ev_organiser_id = request.data['user_ev']                      
        organiser = EventOrganizer.objects.get(pk=ev_organiser_id)
        request.data['user_ev'] = organiser
        serializer = EventOrgSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return redirect(EventListView.as_view)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EventOrganizerDetailView(APIView):
    def get(self,request,pk=None):
        ev = get_object_or_404(EventOrganizer.objects.all(),pk=pk)
        serializer = EventOrgSerializer(ev)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            ev = EventOrganizer.objects.get(pk=pk)
        except EventOrganizer.DoesNotExist:
            return Response({'message':'Event Organizer not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = EventOrgSerializer(ev,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        ev = get_object_or_404(EventOrganizer.objects.all(),pk=pk)
        ev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CustomerListView(APIView):
    def get(self,request):
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        customer_id = request.data['user_cu']                      
        cust = Customer.objects.get(pk=customer_id)
        request.data['user_cu'] = cust                  
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self,request,pk=None):
        cust = get_object_or_404(Customer.objects.all(),pk=pk)
        serializer = CustomerSerializer(cust)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            cust = Tickets.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'message':'Customer not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(cust,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        cust = get_object_or_404(Customer.objects.all(),pk=pk)
        cust.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TicketListView(APIView):
    def get(self,request):
        tkt = Tickets.objects.all()
        serializer = TicketSerializer(tkt,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        ev_organiser_id = request.data['evOrg']                      
        organiser = EventOrganizer.objects.get(pk=ev_organiser_id)
        request.data['evOrg'] = organiser
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(APIView):
    def get(self,request,pk=None):
        tkt = get_object_or_404(Tickets.objects.all(),pk=pk)
        serializer=TicketSerializer(tkt)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            tkt = Tickets.objects.get(pk=pk)
        except Tickets.DoesNotExist:
            return Response({'message':'Ticket not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = TicketSerializer(tkt,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        tkt = get_object_or_404(Tickets.objects.all(),pk=pk)
        tkt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EventListView(APIView):
    def get(self,request):
        ev = Event.objects.all()
        serializer = EventSerializer(ev,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        ev_organiser_id = request.data['evOrg']                      
        organiser = EventOrganizer.objects.get(pk=ev_organiser_id)
        request.data['evOrg'] = organiser
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(APIView):
    def get(self,request,pk=None):
        ev = get_object_or_404(Event.objects.all(),pk=pk)
        print(ev)
        serializer=EventSerializer(ev)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({'message':'event not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event,data=request.data)
        # event = Event.objects.get(pk=pk)
        ticket_entries = event.which_tickets.all()
        l = []
        for ticket in ticket_entries:
            booking_entries = ticket.booking_ref.all()
            for book_ent in booking_entries:
                cust_email = book_ent.cust.email
                l.append(cust_email)

        if serializer.is_valid():
            serializer.save()
            subject = "event update"
            message = "the event for which you booked a ticket has an update"
            recipient_list = l
            send_email_event_update.apply_async(args=[subject, message, recipient_list])
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        ev = get_object_or_404(Event.objects.all(),pk=pk)
        ev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookingListView(APIView):
    def get(self,request):
        bk = Booking.objects.all()
        serializer = BookingSerializer(bk,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        customer_id = request.data['cust']
        customer = Customer.objects.get(pk=customer_id)
        # print(customer)
        request.data['cust'] = customer
        request.data['email'] = customer.email
        # request.data['message'] = "ticket has been booked"
        # print(customer)
        serializer = BookingSerializer(data=request.data)
        # print(serializer)
        # request.data['cust'] = request.user.id
        # serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            # print("-----------------")
            # breakpoint()
            # Tickets.bookShow()
            serializer.save()
            subject = "your ticket has been booked"
            message = "the details of your ticket are as follows"
            recipient_list = [f"{customer.email}"]

            # Trigger the Celery task to send the email
            send_email_ticket_book.apply_async(args=[subject, message, recipient_list])
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookingDetailView(APIView):
    def get(self,request,pk=None):
        bk = get_object_or_404(Booking.objects.all(),pk=pk)
        serializer=BookingSerializer(bk)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        bk = get_object_or_404(Booking.objects.all(),pk=pk)
        # Booking.objects.cancelShow()
        bk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
