from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from .models import EventInstance, EventCategory

class EventCalendar(HTMLCalendar):

    # initiate the calendar with events present
    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)
    
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            cssclass += ' day'
            if date.today() > date(self.year, self.month, day):
                cssclass += ' past'
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            popup = ['<div class="popup">']
            for e in self.events:
                if e.date == date(self.year, self.month, day):
                    popup.append(str(e))
                    popup.append("<button type='button' class='btn btn-primary formbtn' data-bs-toggle='modal' data-bs-target='#exampleModal'>Launch demo modal</button>")
            popup.append('</div>')
            
            return self.day_cell(cssclass, '%d %s' % (day, ''.join(popup)))
        return self.day_cell('noday', '&nbsp;')
    # give first tr css class of .weekdays
    # add clickable/hoverable elements based on class
    # 
    # append html elements that allow you to go to next or previous month
    #
    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        return dict(
            [(date, list(items)) for date, items in groupby(events)]
        )
        # if event is on given day, group it into day's events
        # javascript for on click/on hover for labelled elements to show events + booking form
    
    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)


