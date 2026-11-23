# from datetime import date, datetime

# class Usuario:
#     def __init__(self, nomeUsuario, senha):
#         self.nomeUsuario = nomeUsuario
#         self.senha = senha

#     def mudarSenha(self, novaSenha):
#         self.senha = novaSenha

# class Membro:
#     def __init__(self, nome, dataNascimento, batizado, congregacao, celula, dataCelula, frequencia):
#         self.nome = nome
#         self.dataNascimento = dataNascimento
#         self.batizado = batizado
#         self.congregacao = congregacao
#         self.celula = celula
#         self.dataCelula = dataCelula
#         self.frequencia = frequencia

#     def calcularPorcentFreq(self):
#         def getUltimaSegunda(data):
#             dataOutra = datetime.fromtimestamp(data.timestamp()-((data.weekday()+5)*86400))
#             return dataOutra
    
#         hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
#         # Pegar o tempo decorrido entre a ultima segunda da dataCelula e a ultima segunda a partir de hoje
#         tempo = getUltimaSegunda(hoje).timestamp()-getUltimaSegunda(self.dataCelula).timestamp()
#         frequencias = tempo/604800 # Divide por uma semana para conseguir o número de segundas

#         return self.frequencia/frequencias

#     def addFreq(self):
#         self.frequencia+=1

#     def mudarCelula(self, celula):
#         self.celula = celula

#     def mudarCongregacao(self, congregacao):
#         self.congregacao=congregacao

# class Lider(Membro, Usuario):
#     ...

# class Pastor(Lider, Usuario):
#     ...

# class Admnistrador(Usuario):
#     ...