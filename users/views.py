from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect

class MyBookingsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'my_bookings.html')
