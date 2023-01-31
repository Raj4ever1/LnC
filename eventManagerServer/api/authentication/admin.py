from django.contrib import admin
from .models import User, Role, UserRoleMap

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(UserRoleMap)
class UserRoleMapAdmin(admin.ModelAdmin):
    pass