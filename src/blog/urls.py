"""site_fejesp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Importações do Django
from django.conf.urls import url

# Importações do Projeto
from . import views

urlpatterns = [
    # A url deve serguir o segunte modelo:
    # url(r'^[Nome da URL]/$', views.[Nome da Função da Views], name="[Nome da URL para ser chamada no código]"),
    url(r'^$', views.post_listar, name="listar"),
    url(r'^criar/$', views.post_criar, name="criar"),

    # O (?P<slug>[\w-]+) no URL serve para passar strings (que podem conter quaisquer caracteres ASCII)
    # O nome entre < > (no caso, "slug") deve ser o mesmo do parâmetro da função da views correspondente.
    url(r'^(?P<slug>[\w-]+)/$', views.post_detalhar, name="detalhar"),
    url(r'^(?P<slug>[\w-]+)/editar/$', views.post_editar, name="editar"),
    url(r'^(?P<slug>[\w-]+)/deletar/$', views.post_deletar, name="deletar"),

    # O (?P<id>\d+) no URL serve para passar números apenas.
    # O nome entre < > (no caso, "id_post") deve ser o mesmo do parâmetro da função da views correspondente.

    # url(r'^(?P<id_post>\d+)/$', views.post_detalhar, name="detalhar"),
    # url(r'^(?P<id_post>\d+)/editar/$', views.post_editar, name="editar"),
    # url(r'^(?P<id_post>\d+)/deletar/$', views.post_deletar, name="deletar"),
]
