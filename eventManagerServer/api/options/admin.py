from django.contrib import admin

from .models import Option


# Register your models here.
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass