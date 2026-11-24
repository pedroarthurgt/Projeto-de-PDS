from django.shortcuts import render
from .models import Celula

# Create your views here.
def multiplicarCelula(self):
    celula = Celula(self.nome, self.numero+1, self.lider)
    celula.save()
    return celula