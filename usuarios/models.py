from django.db import models

# Create your models here.
from datetime import date, datetime

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=30, primary_key=True)
    senha = models.CharField(max_length=20)

    class Meta:
        abstract=True

    @classmethod
    def criar(cls, nomeUsuario, senha):
        usuario = cls(nomeUsuario=nomeUsuario, senha=senha)
        return usuario

    @classmethod
    def mudarSenha(self, novaSenha):
        self.senha = novaSenha

    @classmethod
    def deletar(self):
        self.delete()
        return True


class Membro(models.Model):
    nome = models.CharField(max_length=40)
    dataNascimento = models.DateField
    batizado = models.BooleanField
    congregacao = models.CharField(max_length=30)
    celula = models.ForeignKey('celulas.Celula', on_delete=models.SET_NULL, null=True)
    dataCelula = models.DateField
    frequencia = models.IntegerField

    @classmethod
    def criar(cls, nome, dataNascimento, batizado, congregacao, celula, dataCelula, frequencia):
        membro = cls(nome=nome, dataNascimento=dataNascimento, batizado=batizado, congregacao=congregacao, celula=celula, dataCelula=dataCelula, frequencia=frequencia)

    @classmethod
    def deletar(self):
        self.delete()
        return True

    @classmethod
    def addFreq(self):
        self.frequencia+=1
        self.save()

    @classmethod
    def mudarCelula(self, celula):
        self.celula = celula
        self.save()

    @classmethod
    def mudarCongregacao(self, congregacao):
        self.congregacao=congregacao
        self.save()

class Lider(Membro, Usuario):
    ...

class Pastor(Lider, Usuario):
    ...

class Admnistrador(Usuario):
    ...