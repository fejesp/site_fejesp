# Importações do Django
from django import forms

# Importações do Projeto
from .models import Empresa_Parceira


class Empresa_ParceiraForm(forms.ModelForm):
    """[DLL:2016/03/13] Formulário relativo a classe Empresa_Parceira.
    Todo formulário da classe Empresa_Parceira seguirá os parâmetros definidos nesta classe Empresa_ParceiraForm"""

    # A classe Meta serve para tudo que não é um atributo ou método. Apenas para "descrever" a classe melhor
    class Meta:
        model = Empresa_Parceira
        fields = [
            # Coloque os fields que serão exibidos no forms aqui
        ]
