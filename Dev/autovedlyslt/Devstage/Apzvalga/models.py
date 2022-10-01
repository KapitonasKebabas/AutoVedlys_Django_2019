from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class infoSustojimai(models.Model):
    data = models.DateField()
    papildyta = models.CharField(max_length=6)
    odometras = models.CharField(max_length=6)
    suma = models.CharField(max_length=6)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    