from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

class EventCalendar(HTMLCalendar):

    # initiate the calendar with events present
    def __init__(self, events):
        super(EventCalendar, self).init()
        self.events = self.group_by_day(events)

    # give first tr css class of .weekdays
    # add clickable/hoverable elements based on class
    # 
    # 
    #
    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.performed_at.day
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )


