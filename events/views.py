from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import EventCategory, EventInstance
import calendar as cal
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

class CategoryListView(generic.ListView):
    context_object_name = "category_list"
    model = EventCategory
    template_name = "index.html"

    def get_queryset(self,*args,**kwargs):
       qs=super().get_queryset(*args, **kwargs)
       return qs

class CalendarView(View):
    def get(self, request, year, month):
        month = month.capitalize()
        month_number = list(cal.month_name).index(month)
        month_number = int(month_number)
        calendar = HTMLCalendar().formatmonth(year, month_number)
        now = datetime.now()
        #current_year = now.year()

        return render(
                request, "calendar.html",
                {
                    "calendar": calendar,
                    "year": year,
                    "month": month,
                    "month_number": month_number,
                    #"current_year": current_year,
                },)
