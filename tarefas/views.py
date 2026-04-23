from django.shortcuts import render, redirect # importamos a função render para renderizar os templates HTML e a função redirect para redirecionar o usuário para outra página após o envio do formulário
from django.http import HttpRequest #importar a classe HttpRequest para tipar o parâmetro da função
from .forms import TarefasForm
# Create your views here.

def tarefas_home(request):
    # é possível passar variáveis para o template HTML através de um dicionário
    contexto = {
        "nome" : "Luis Felipe",
    }
    
    return render(request, 'tarefas/home.html', contexto)

def registrar_tarefas(request:HttpRequest):
    # Tratamento de dados enviados pelo formulário
    if request.method == 'POST':
        formulario = TarefasForm(request.POST) #instância do formulário preenchida com os dados enviados pelo usuário
        if formulario.is_valid(): #verificar se os dados enviados são válidos de acordo com as regras definidas no formulário
            formulario.save() #salvar os dados no banco de dados (cria uma nova instância do modelo tarefaModel com os dados do formulário e salva no banco de dados)
            return redirect("tarefas:home") #redirecionar o usuário para a página inicial das tarefas após o envio do formulário
    
    contexto = {
        "form": TarefasForm #instância do formulário para ser renderizada no template HTML
    }
    
    return render(request, 'tarefas/registrar.html', contexto)