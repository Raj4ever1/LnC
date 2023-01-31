from django.contrib import admin

from api.notification.models import Notification

# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
