from django.db import models

from api.utills.constraints import TransactionStatus
from api.team.models import Participant
from api.authentication.models import UserRoleMap

# Create your models here.
class Match(models.Model):
    status_options = ((element.value, element.name) for element in TransactionStatus)
    status = models.CharField(max_length=20, choices=status_options, default=TransactionStatus.NOT_STARTED)
    winner = models.ForeignKey(Participant,on_delete=models.CASCADE)
    refree = models.ForeignKey(UserRoleMap,on_delete=models.CASCADE)
    
class MatchParticipantMap(models.Model):
    match_id = models.ForeignKey(Match,on_delete=models.CASCADE)
    participant_id = models.ForeignKey(Participant,on_delete=models.CASCADE)
