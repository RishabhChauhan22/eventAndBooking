"""
URL configuration for eventAndBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookingApi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/',views.UserListView.as_view()),
    # path('user/<str:pk>',views.UserDetailView.as_view()),
    path('customer/',views.CustomerListView.as_view()),
    path('customer/<str:pk>/',views.CustomerDetailView.as_view()),
    path('eventOrganizer/',views.EventOrganizerListView.as_view()),
    path('eventOrganizer/<str:pk>/',views.EventOrganizerDetailView.as_view()),
    path('ticket/',views.TicketListView.as_view()),
    path('ticket/<str:pk>/',views.TicketDetailView.as_view()),
    path('event/',views.EventListView.as_view()),
    path('event/<str:pk>',views.EventDetailView.as_view()),
    path('booking/',views.BookingListView.as_view()),
    path('booking/<str:pk>',views.BookingDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)