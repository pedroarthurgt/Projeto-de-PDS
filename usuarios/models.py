from django.db import models

# Create your models here.
from datetime import date, datetime

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)

class Membro(models.Model):
    nome = models.CharField(max_length=40)
    dataNascimento = models.DateField
    batizado = models.BooleanField
    congregacao = models.CharField(max_length=30)
    celula = models.ForeignKey('celulas.Celula')
    dataCelula = models.DateField
    frequencia = models.IntegerField

class Lider(Membro, Usuario):
    ...

class Pastor(Lider, Usuario):
    ...

class Admnistrador(Usuario):
    ...