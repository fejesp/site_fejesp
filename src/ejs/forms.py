# Importações do Django
from django import forms

# Importações do Projeto
from .models import EJ


class EJForm(forms.ModelForm):
    """[DLL:2016/03/13] Formulário relativo a classe EJ.
    Todo formulário da classe EJ seguirá os parâmetros definidos nesta classe EJForm"""

    # A classe Meta serve para tudo que não é um atributo ou método. Apenas para "descrever" a classe melhor
    class Meta:
        model = EJ
        fields = [
            # Coloque os fields que serão exibidos no forms aqui
        ]
