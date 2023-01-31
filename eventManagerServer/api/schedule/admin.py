from django.contrib import admin

from api.schedule.models import Schedule, Room, EventScheduleMap

# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(EventScheduleMap)
class EventScheduleMapAdmin(admin.ModelAdmin):
    pass
