from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Membro, Lider, Pastor, Admnistrador

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        nomeUsuario=request.POST.get("usuario").strip()
        senha=request.POST.get("senha").strip()

        usuario = authenticate(request, username=nomeUsuario, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def removerMembro(request):
    if request.method == 'POST':
        nome=request.POST.get("nome")
        dataNascimento=request.POST.get("dataNascimento")

        membro = Membro.procurarPorNomeDataNascimento(nome, dataNascimento)
        if membro is not None:
            membro.delete()

def removerLider(request):
    if request.method == 'POST':
        nome=request.POST.get("nome")
        dataNascimento=request.POST.get("dataNascimento")

        lider = Lider.procurarPorNomeDataNascimento(nome, dataNascimento)
        if lider is not None:
            lider.delete()

def removerPastor(request):
    if request.method == 'POST':
        nome=request.POST.get("nome")
        dataNascimento=request.POST.get("dataNascimento")

        pastor = Pastor.procurarPorNomeDataNascimento(nome, dataNascimento)
        if Pastor is not None:
            Pastor.delete()

def removerAdmnistrador(request):
    if request.method == 'POST':
        nome=request.POST.get("usuario")

        admnistrador = Admnistrador.procurarPorNome(nome)
        if admnistrador is not None:
            admnistrador.delete()
        

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
def cadastroMembro(request):
    if request.method == 'POST':
        nome=request.POST.get("nome")
        dataNascimento=request.POST.get("dataNascimento")
        
    return render(request, 'usuarios/cadastroMembro.html')