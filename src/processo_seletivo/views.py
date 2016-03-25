# Importações do Django
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render

# Importações do Projeto
from .models import Cargo
from .forms import CargoForm

def cargo_criar(request):
    """[DLL:2016/03/17] Função criar: cria novas instâncias do processo seletivo. Utiliza a mesma página que a função cargo_editar.
    Só é possível criar a instância numa página específica e apenas o administrador poderá criar novas instâncias do processo seletivo."""
    pass
    # return render(request, "processo_seletivo/cargo_form.html", locals())


def processo_seletivo_listar(request):
    """[DLL:2016/03/13] Mostra todas as instancias do processo seletivo.
    Apenas o administrador poderá ver esta lista de instancias. O usuário comum só deve ter acesso ao último processo seletivo"""
    pass
    # return render(request, "processo_seletivo/processo_seletivo_listar.html", locals())


def processo_seletivo_detalhar(request):
    """[DLL:2016/03/17] Filtra apenas uma instância e um tipo de processo seletivo (exemplo: PS Assessores 2016.1).
    Exibe essa
    Só é possível criar a instância numa página específica e apenas o administrador poderá criar novas instâncias do processo seletivo."""
    pass
    # return render(request, "processo_seletivo/processo_seletivo_detalhar.html", locals())


def cargo_editar(request, id):
    """[DLL:2016/03/17] Função editar: edita os cargos do processo seletivo. Utiliza a mesma página que a função cargo_criar
    Só é possível editar o cargo numa página específica e apenas o administrador poderá editar os cargos."""
    pass
    # return render(request, "processo_seletivo/cargo_form.html", locals())


def cargo_deletar(request, id):
    """[DLL:2016/03/17] Função deletar: apaga os cargos do processo.
    Só é possível apagar um de cada vez e apenas o administrador poderá deletar os cargos."""
    pass
    # return redirect("processo_seletivo:listar")


def processo_seletivo_deletar(request, instancia, tipo):
    """[DLL:2016/03/17] Função deletar processo seletivo:
    Filtra os cargos por instância e tipo de processo seletivo (exemplo: PS Coordenadores 2016.1) e deleta todos os correspondentes.
    Apenas o administrador poderá deletar os cargos."""
    pass
    # return redirect("processo_seletivo:listar")
