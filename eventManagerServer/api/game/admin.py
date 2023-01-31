from django.contrib import admin

from .models import Game, Rule
# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass