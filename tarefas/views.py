from django.shortcuts import render #importar a função render para renderizar templates HTML
from django.http import HttpResponse

# Create your views here.

def tarefas_home(request):
    # é possível passar variáveis para o template HTML através de um dicionário
    contexto = {
        "nome" : "Luis Felipe",
    }
    
    return render(request, 'tarefas/home.html', contexto)

def registrar_tarefas(request):
    return HttpResponse("<h1>Registre aqui uma nova tarefa</h1>")