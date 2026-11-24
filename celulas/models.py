from django.db import models

# Create your models here.
class Celula(models.Model):
    nome = models.CharField(max_length=20)
    numero = models.IntegerField()  
    lider = models.ForeignKey('usuarios.Lider', on_delete=models.SET_NULL, related_name='celulas_lideradas', null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'numero'], name='unique_nome_numero_combination'
            )
        ]

    @classmethod
    def criar(cls, nome, numero, lider):
        celula = cls(nome=nome, numero=numero, lider=lider)
    
    @classmethod
    def multiplicarCelula(self):
        celula = Celula(self.nome, self.numero+1, self.lider)

    @classmethod
    def mudarLider(self, lider):
        self.lider = lider