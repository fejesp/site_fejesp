# Importações do Django
from django import forms

# Importações do Projeto
from .models import Post


class PostForm(forms.ModelForm):
    """[DLL:2016/03/13] Formulário relativo a classe Post.
    Todo formulário da classe Post seguirá os parâmetros definidos nesta classe PostForm"""

    # A classe Meta serve para tudo que não é um atributo ou método. Apenas para "descrever" a classe melhor
    class Meta:
        model = Post
        fields = [
            "titulo",
            "autor",
            "imagem",
            "rascunho",
            "data_publicacao",
            "conteudo",
        ]

        # [DLL:2016/03/16] Forms agora estão no estilo do Template
        # Os widgets servem, entre outras coisas, para passar uma classe específica no form e dar match com a classe de estilo do CSS
        # Solução encontrada em:
        # http://stackoverflow.com/questions/5827590/css-styling-in-django-forms
        # https://docs.djangoproject.com/ja/1.9/ref/forms/widgets/#built-in-widgets
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
        }
