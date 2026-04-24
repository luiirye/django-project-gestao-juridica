from django.shortcuts import render, redirect, get_object_or_404 # importamos a função render para renderizar os templates HTML e a função redirect para redirecionar o usuário para outra página após o envio do formulário
from django.http import HttpRequest #importar a classe HttpRequest para tipar o parâmetro da função
from .forms import TarefasForm
from .models import tarefaModel
# Create your views here.

def tarefas_home(request):
    # é possível passar variáveis para o template HTML através de um dicionário
    contexto = {
        "nome" : "Luis Felipe",
        "tarefas": tarefaModel.objects.all() #consulta ao banco de dados para obter todas as tarefas cadastradas e passar para o template HTML
    }
    
    return render(request, 'tarefas/home.html', contexto)

def registrar_tarefas(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
 
    
    contexto = {
        "form": TarefasForm #instância do formulário para ser renderizada no template HTML
    }
    
    return render(request, 'tarefas/registrar.html', contexto)

def remover_tarefas(request:HttpRequest, id):
    tarefa = get_object_or_404(tarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")