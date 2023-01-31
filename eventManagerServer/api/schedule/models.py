from django.db import models

from api.match.models import Match
from api.event.models import EventGameMap

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)

class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match,on_delete=models.CASCADE)
    round = models.IntegerField()
    
class EventScheduleMap(models.Model):
    event_game_id = models.ForeignKey(EventGameMap,on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule,on_delete=models.CASCADE)