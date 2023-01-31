from django.contrib import admin
from .models import Participant, Team, TeamMember
# Register your models here.
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass