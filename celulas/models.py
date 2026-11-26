from django.db import models
from copy import deepcopy
# Create your models here.
class Celula(models.Model):
    nome = models.CharField(max_length=20)
    numero = models.IntegerField()  
    lider = models.ForeignKey('pessoas.Lider', on_delete=models.SET_NULL, related_name='celulas_lideradas', null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'numero'], name='unique_nome_numero_combination'
            )
        ]

    @classmethod
    def criar(cls, nome, numero, lider):
        celula = cls(nome=nome, numero=numero, lider=lider)
        return celula
    
    def mudarLider(self, lider):
        self.lider = lider
        self.save()

    def deletar(self):
        self.delete()
        return True

    def adicionar(self):
        self.save()
        return True

    def procurarPorNome(nome):
        celula = Celula.objects.filter(nome__icontains=nome)
        return celula

    def procurarPorNomeNumero(nome, numero):
        celula = Celula.objects.filter(nome__icontains=nome)
        celula = celula.filter(numero__icontains=numero)
        return celula

    def multiplicarCelula(self):
        novaCelula = deepcopy(self)
        novaCelula['numero']+=1
        novaCelula.save()