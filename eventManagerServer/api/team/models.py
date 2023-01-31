from django.db import models

from api.event.models import EventGameMap
from api.authentication.models import UserRoleMap

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    event_game_map_id = models.ForeignKey(EventGameMap,on_delete=models.CASCADE)



class Participant(models.Model):
    event_game_map_id = models.ForeignKey(EventGameMap,on_delete=models.CASCADE)
    user_role_map_id = models.ForeignKey(UserRoleMap,on_delete=models.CASCADE,null = True,limit_choices_to={'role_id':3},blank = True)
    team_id = models.ForeignKey(Team,on_delete=models.CASCADE,null = True,blank = True)

class TeamMember(models.Model):
    team_id = models.ForeignKey(Team,on_delete=models.CASCADE)
    user_role_map_id = models.ForeignKey(UserRoleMap,on_delete=models.CASCADE)
    