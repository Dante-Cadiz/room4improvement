from django.contrib import admin
from .models import EventCategory, EventInstance

# Register your models here.

@admin.register(EventCategory)
class EventInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    pass