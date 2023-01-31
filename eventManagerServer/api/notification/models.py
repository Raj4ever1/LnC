from django.db import models
from ..authentication.models import User
# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)