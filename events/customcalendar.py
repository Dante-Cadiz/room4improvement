from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from .models import EventInstance, EventCategory

class EventCalendar(HTMLCalendar):

    # initiate the calendar with events present
    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)
    
    #def formatday(self, day, weekday):
        #if EventInstance
    # give first tr css class of .weekdays
    # add clickable/hoverable elements based on class
    # 
    # append html elements that allow you to go to next or previous month
    #
    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        pass
        #field = event
        #return dict(
            #[(day, list(items)) for day, items in groupby(events, field)]
        #)


