# Importações do Django
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render

# Importações do Projeto
from .models import EJ
from .forms import EJForm


def ej_criar(request):
    """[DLL:2016/03/17] Função criar: cria/cadastra Empresas Juniores.
    Deve haver 2 jeitos de cadastrar uma EJ:
        Um usuário cadastra a EJ: Neste, ele não pode selecionar se a EJ é federada ou não, e o padrão é que não seja. Utiliza um form diferente do administrador.
        O administrador cadastra a EJ: Utiliza a mesma página que a função ej_editar.
    Só é possível criar uma nova Empresas Juniores numa página específica."""
    pass
    # return render(request, "ejs/ej_form.html", locals())


def ej_listar(request):
    """[DLL:2016/03/13] Mostra todas as empresas cadastradas e aprovadas.
    Deve conter também um filtro de pesquisa de acordo com a área de atuação, portifólio e endereço (Cidade)"""
    pass
    # return render(request, "ejs/ej_listar.html", locals())


def ej_pendente_listar(request):
    """[DLL:2016/03/13] Mostra todas as empresas cadastradas que estão aguardando aprovação do administrador para ser exibidas no site.
    Apenas o administrador deverá ter acesso a essa página."""
    pass
    # return render(request, "ejs/ej_listar.html", locals())


def ej_editar(request, id):
    """[DLL:2016/03/17] Função editar: edita as informações das EJs. Utiliza a mesma página que a função ej_criar ()
    Só é possível editar numa página específica, a qual apenas o administrador terá acesso."""
    pass
    # return render(request, "ejs/ej_form.html", locals())


def ej_deletar(request, id):
    """[DLL:2016/03/17] Função deletar: apaga uma EJ.
    Só é possível apagar um de cada vez e apenas o administrador poderá deletar."""
    pass
    # return redirect("ejs:listar")
