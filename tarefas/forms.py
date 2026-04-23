from django import forms
from .models import tarefaModel

class TarefasForm(forms.ModelForm):
    class Meta: #Classe de configuração do formulário
        model = tarefaModel #modelo que o formulário irá representar
        fields = [
            'nome',
            'descricao',
            'concluido',
        ]