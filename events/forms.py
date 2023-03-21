from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event']
        ## get event
        ## get booker from user registered
        