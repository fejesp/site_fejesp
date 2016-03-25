# Importações do Django
from django import forms

# Importações do Projeto
from .models import Cargo


class CargoForm(forms.ModelForm):
    """[DLL:2016/03/13] Formulário relativo a classe Cargo.
    Todo formulário da classe Cargos seguirá os parâmetros definidos nesta classe CargoForm"""

    # A classe Meta serve para tudo que não é um atributo ou método. Apenas para "descrever" a classe melhor
    class Meta:
        model = Cargo
        fields = [
            # Coloque os fields que serão exibidos no forms aqui
        ]
