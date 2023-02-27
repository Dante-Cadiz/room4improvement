from django.db import models
from users.models import SiteUser, Admin

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Upcoming'), (2, 'Past'))

TIMETABLE = ()

#class Timeslot(models.Model):
    
    #max_events = 


class EventInstance(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(Admin, on_delete=models.RESTRICT,
                               related_name="events", null=True)
    #featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    max_attendees = models.IntegerField(null=True)
    start_time = models.DateTimeField(choices=TIMETABLE)
    # set start time based on selected timetable object
    duration = models.DurationField(null=True) #in minutes
    attendees = models.ManyToManyField(SiteUser, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    #def determine_end_time(self):
        # return start_time += duration


    def __str__(self):
        start = self.start_time.strftime("%-d/%-m, %H:%M")
        return f"{self.title}: {start}"