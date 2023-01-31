from django.contrib import admin
from .models import Event, EventGameMap, EventUserMap
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
@admin.register(EventGameMap)
class EventGameMapAdmin(admin.ModelAdmin):
    pass
@admin.register(EventUserMap)
class EventUserMappAdmin(admin.ModelAdmin):
    pass
