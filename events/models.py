from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Upcoming'), (2, 'Past'))


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    #manytomany field with event instances

    class Meta:
        verbose_name_plural = "Event Categories"
    
    def __str__(self):
        return self.name
    

class EventInstance(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.RESTRICT,
                               related_name="events", null=True)
    #featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    max_attendees = models.IntegerField(null=True)
    date = models.DateField(null=True)
    start_time = models.TimeField()
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE,
             related_name="events", null=True)
    duration = models.DurationField(default=timedelta()) #in minutes
    attendees = models.ManyToManyField(User, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def determine_end_time(self):
        return start_time + timedelta(duration)


    def __str__(self):
        start = self.start_time.strftime("%H:%M")
        return f"{self.title}: {start}"

 ## get_absolute_url method

class Booking(models.Model):
    event = models.ForeignKey(EventInstance, on_delete=models.CASCADE,
                              related_name='event', blank=True)
    booker = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='booker', blank=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE,
    related_name="category", blank=True)