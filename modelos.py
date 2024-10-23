# No arquivo models.py dentro do aplicativo
from django.db import models

class MeuModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.DateField()
