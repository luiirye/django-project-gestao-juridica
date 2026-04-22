from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tarefas_home(request):
    return HttpResponse("<h1>Aqui estão suas tarefas listadas</h1>")

def registrar_tarefas(request):
    return HttpResponse("<h1>Registre aqui uma nova tarefa</h1>")