from django.db import models

# Create your models here.
class Celula(models.Model):
    nome = models.CharField(max_length=20)
    numero = models.IntegerField()
    lider = models.CharField()