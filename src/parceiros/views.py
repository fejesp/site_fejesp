# Importações do Django
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render

# Importações do Projeto
from .models import Empresa_Parceira
from .forms import Empresa_ParceiraForm


def parceiro_criar(request):
    """[DLL:2016/03/17] Função criar: cria/cadastra novas Empresas Parceiras. Utiliza a mesma página que a função parceiro_editar.
    Só é possível criar uma nova Empresa Parceira numa página específica e a qual apenas o administrador terá acesso."""
    pass
    # return render(request, "parceiros/parceiro_form.html", locals())


def parceiro_listar(request):
    """[DLL:2016/03/13] Mostra todas as empresas cadastradas."""
    pass
    # return render(request, "parceiros/parceiro_listar.html", locals())


def parceiro_editar(request, id):
    """[DLL:2016/03/17] Função editar: edita as informações das Empresas Parceiras. Utiliza a mesma página que a função parceiro_criar
    Só é possível editar numa página específica, a qual apenas o administrador terá acesso."""
    pass
    # return render(request, "parceiros/parceiro_form.html", locals())


def parceiro_deletar(request, id):
    """[DLL:2016/03/17] Função deletar: apaga as Empresas Parceiras.
    Só é possível apagar um de cada vez e apenas o administrador poderá deletar."""
    pass
    # return redirect("parceiros:listar")
