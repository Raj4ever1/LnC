from django.db import models

from api.game.models import Game
from api.authentication.models import UserRoleMap

from ..utills.constraints import TransactionStatus

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200,default='')
    status_options = ((element.value, element.name) for element in TransactionStatus)
    status = models.CharField(max_length=20, choices=status_options, default=TransactionStatus.NOT_STARTED)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    max_players = models.IntegerField(default=0)
    min_players = models.IntegerField(default=0)
    USERNAME_FIELD = 'name'

class EventGameMap(models.Model):
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game,on_delete=models.CASCADE)
    status_options = ((element.value, element.name) for element in TransactionStatus)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=status_options, default=TransactionStatus.NOT_STARTED)
    max_players = models.IntegerField(default=0)
    min_players = models.IntegerField(default=0)
    
class EventUserMap(models.Model):
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserRoleMap,on_delete=models.CASCADE,limit_choices_to={'role_id':2})