from django.contrib import admin
from .models import EventInstance

# Register your models here.

@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    pass