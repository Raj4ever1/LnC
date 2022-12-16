from django.db import models

from api.authentication.models import Role


# Create your models here.
class Option(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    option = models.CharField(max_length=100)