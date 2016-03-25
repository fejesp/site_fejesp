# Importações do Django
from django.db import models


class EJ(models.Model):
    """[DLL:2016/03/18] Classe que modela as informações deve conter.
    Cada cargo ficará "solto" e deverá ser filtrado depois para as diferentes instancias e tipos de cargo que
    Atributos:
        Nome da empresa;
        Logo;
        Telefone;
        Email;
        Site;
        Endereço;
        Federada;
        Portfólio;
        Área de Atuação;
        Descrição;
        Aprovada; (Somente exibe as EJs aprovadas pelo administrador)
    Métodos:
        __str__
        get_absolute_url
    """
    pass
