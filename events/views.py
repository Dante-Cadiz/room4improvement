from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import EventCategory, EventInstance
import calendar as cal
from .customcalendar import EventCalendar
from datetime import datetime

# Create your views here.

class CategoryListView(generic.ListView):
    context_object_name = "category_list"
    model = EventCategory
    template_name = "index.html"

    def get_queryset(self,*args,**kwargs):
       qs=super().get_queryset(*args, **kwargs)
       return qs

class MyBookingsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'my_bookings.html')

class CategoryView(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(EventCategory, slug=slug)
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        events = EventInstance.objects.filter(category=category)
        calendar = EventCalendar(events).formatmonth(current_year, current_month)

        return render(
                request, "category.html",
                {
                    "category": category,
                    'events': events,
                    "calendar": calendar,
                },)

class MakeBooking(View):

    def post(self, request, slug, *args, **kwargs):
        instances = EventInstance.objects.all()
        instance = get_object_or_404(instance, id=self.kwargs['pk'])
        category = get_object_or_404(slug=slug)
        instance.attendees.add(request.user)
        Booking.objects.create(category=category, booker=self.request.user, instance=instance)
        messages.add_message(request, messages.SUCCESS,
                             "Event successfully booked")
        return HttpResponseRedirect(reverse('category', args=[slug]))

