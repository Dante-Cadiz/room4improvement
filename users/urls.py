from . import views
from django.urls import path

urlpatterns = [
    path('my_bookings', views.MyBookingsView.as_view(), name='my_bookings'),
]