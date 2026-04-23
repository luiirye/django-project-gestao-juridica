from django.db import models

# Create your models here.
# criamos classes e esssas classes serão traduzidas em tabelas no banco de dados

class terefaModel(models.Model): #precisa herdar de models.Model para ser reconhecida como um modelo do Django
    nome = models.CharField(max_length=100) #campo de texto com limite de 100 caracteres
    descricao = models.TextField(null = True, blank = True) #campo de texto não obrigatório
    concluido = models.BooleanField(default=False) #campo booleano para indicar se a tarefa foi concluída ou não
    data_criacao = models.DateTimeField(auto_now_add=True) #campo de data e hora que é preenchido automaticamente com a data e hora atual quando a tarefa é criada
    
    def __str__(self):
        return self.nome #método que retorna o nome da tarefa quando a instância do modelo for convertida para string (ex: no admin do Django)