# Importações do Django
from django.contrib import admin

# Importações do Projeto
from .models import Empresa_Parceira


class Empresa_ParceiraAdmin(admin.ModelAdmin):
    """[DLL:2016/03/13] Esta classe edita a página que lista os objetos da classe Empresa_Parceira no admin,
    tornando mais fácil a visualização e edição.
    Para mais informações sobre as opções de visualização,
    visite: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#modeladmin-options"""
    class Meta:
        model = Empresa_Parceira

    # Mostram esses campos na lista de objetos da classe
    #list_display = ["titulo", "ultima_atualizacao", "data_criacao"]

    # Coloca o campo como clicável
    #list_display_links = ["ultima_atualizacao"]

    # Adiciona filtro nos campos
    #list_filter = ["ultima_atualizacao", "data_criacao"]

    # Torna os campos pesquisáveis
    #search_fields = ["titulo", "conteudo"]

    # Torna o campo editável
    #list_editable = ["titulo"]

# Sem essa linha, a classe Empresa_Parceira não aparece no admin
admin.site.register(Empresa_Parceira, Empresa_ParceiraAdmin)
