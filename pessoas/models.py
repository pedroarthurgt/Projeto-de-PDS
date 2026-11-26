from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from datetime import date, datetime

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=30, primary_key=True)
    senha = models.CharField(max_length=20)

    class Meta:
        abstract=True

    @classmethod
    def criar(cls, nomeUsuario, senha):
        usuario = cls(nomeUsuario=nomeUsuario, senha=str(senha))
        return usuario

    def mudarSenha(self, novaSenha):
        self.senha = novaSenha

    def adicionarUsuario(self):
        usuario = User.objects.create_user(username=self.nomeUsuario, password=self.senha)
        self.usuario = usuario
        self.save()
        return True
    
    def deletar(self):
        self.delete()
        return True

    def procurarPorNome(nome):
        usuario = Usuario.objects.filter(nome__icontains=nome)
        return usuario


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

    def adicionarMembro(self):
        self.save()
        return True

    def deletar(self):
        self.delete()
        return True

    def addFreq(self):
        self.frequencia+=1
        self.save()

    def procurarPorNome(nome):
        membro = Membro.objects.filter(nome__icontains=nome)
        return membro

    def procurarPorNomeDataNascimento(nome, dataNascimento):
        membro = Membro.objects.filter(nome__icontains=nome, dataNascimento__icontains=dataNascimento)
        return membro

    def mudarCelula(self, celula):
        self.celula = celula
        self.save()

    def mudarCongregacao(self, congregacao):
        self.congregacao=congregacao
        self.save()

    @classmethod
    def calcularPorcentFreq(self):
        def getUltimaSegunda(data):
            dataOutra = datetime.fromtimestamp(data.timestamp()-((data.weekday()+5)*86400))
            return dataOutra
        
        hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        # Pegar o tempo decorrido entre a ultima segunda da dataCelula e a ultima segunda a partir de hoje
        tempo = getUltimaSegunda(hoje).timestamp()-getUltimaSegunda(self.dataCelula).timestamp()
        frequencias = tempo/604800 # Divide por uma semana para conseguir o número de segundas

        return self.frequencia/frequencias # Retorna a % da frequência


class Lider(Membro, Usuario):
    ...

class Pastor(Lider, Usuario):
    ...

class Admnistrador(Usuario):
    ...