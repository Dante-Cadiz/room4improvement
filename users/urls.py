from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyBookingsView.as_view(), name='my_bookings'),
]