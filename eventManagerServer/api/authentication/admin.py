from django.contrib import admin
from .models import User, Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass