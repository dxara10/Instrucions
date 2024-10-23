from django.db import models

class MeuModelo(models.Model):
    meu_charfield = models.CharField(max_length=100)
