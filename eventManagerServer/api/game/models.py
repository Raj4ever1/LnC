from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.TimeField(max_length=300)
    no_of_players = models.IntegerField(default=0)
    is_indoor = models.BooleanField(default=True)
    is_team_game = models.BooleanField(default=True)    
    
class Rule(models.Model):
    game_id = models.ForeignKey(Game,on_delete=models.CASCADE)
    rule = models.CharField(max_length=200)