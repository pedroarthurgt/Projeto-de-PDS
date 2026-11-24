from django.db import models

# Create your models here.
from datetime import date, datetime

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)

    @classmethod
    def criar(cls, nomeUsuario, senha):
        usuario = cls(nomeUsuario=nomeUsuario, senha=senha)
        return usuario

    @classmethod
    def mudarSenha(self, novaSenha):
        self.senha = novaSenha


class Membro(models.Model):
    nome = models.CharField(max_length=40)
    dataNascimento = models.DateField
    batizado = models.BooleanField
    congregacao = models.CharField(max_length=30)
    celula = models.ForeignKey('celulas.Celula')
    dataCelula = models.DateField
    frequencia = models.IntegerField

    @classmethod
    def criar(cls, nome, dataNascimento, batizado, congregacao, celula, dataCelula, frequencia):
        membro = cls(nome=nome, dataNascimento=dataNascimento, batizado=batizado, congregacao=congregacao, celula=celula, dataCelula=dataCelula, frequencia=frequencia)

    @classmethod
    def calcularPorcentFreq(self):
        def getUltimaSegunda(data):
            dataOutra = datetime.fromtimestamp(data.timestamp()-((data.weekday()+5)*86400))
            return dataOutra
    
        hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        # Pegar o tempo decorrido entre a ultima segunda da dataCelula e a ultima segunda a partir de hoje
        tempo = getUltimaSegunda(hoje).timestamp()-getUltimaSegunda(self.dataCelula).timestamp()
        frequencias = tempo/604800 # Divide por uma semana para conseguir o número de segundas

        return self.frequencia/frequencias

    @classmethod
    def addFreq(self):
        self.frequencia+=1

    @classmethod
    def mudarCelula(self, celula):
        self.celula = celula

    @classmethod
    def mudarCongregacao(self, congregacao):
        self.congregacao=congregacao

class Lider(Membro, Usuario):
    ...

class Pastor(Lider, Usuario):
    ...

class Admnistrador(Usuario):
    ...