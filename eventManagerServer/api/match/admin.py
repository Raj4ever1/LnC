from django.contrib import admin

from api.match.models import MatchParticipantMap, Match

# Register your models here.
@admin.register(MatchParticipantMap)
class MatchParticipantMapAdmin(admin.ModelAdmin):
    pass
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
