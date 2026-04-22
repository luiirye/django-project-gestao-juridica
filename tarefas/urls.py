# Rotas relacionadas ao app "tarefas"
from django.urls import path
from . import views

urlpatterns = [
    # aqui serão definidas as rotas relacionadas ao app "tarefas"
    path('', views.tarefas_home, name='tarefas_home'),
    path('registrar/', views.registrar_tarefas, name='registrar_tarefas'),
]
