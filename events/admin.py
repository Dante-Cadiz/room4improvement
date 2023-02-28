from django.contrib import admin
from .models import EventCategory, EventInstance

# Register your models here.

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass

@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    pass