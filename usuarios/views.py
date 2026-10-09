from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        return redirect('dashboard')  # por enquanto, sem validar nada
    return render(request, 'usuarios/login.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
def cadastroMembro(request):
    return render(request, 'usuarios/cadastroMembro.html')