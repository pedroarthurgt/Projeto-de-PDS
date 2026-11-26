from django.apps import AppConfig


class PessoasConfig(AppConfig):
    name = 'pessoas'

# class Usuario:
#     def __init__(self, nomeUsuario, senha):
#         self.nomeUsuario = nomeUsuario
#         self.senha = senha


# class Membro:
#     def __init__(self, nome, dataNascimento, batizado, congregacao, celula, dataCelula, frequencia):
#         self.nome = nome
#         self.dataNascimento = dataNascimento
#         self.batizado = batizado
#         self.congregacao = congregacao
#         self.celula = celula
#         self.dataCelula = dataCelula
#         self.frequencia = frequencia



# class Lider(Membro, Usuario):
#     ...

# class Pastor(Lider, Usuario):
#     ...

# class Admnistrador(Usuario):
#     ...