# Importações do Django
from django.db import models


class Cargo(models.Model):
    """[DLL:2016/03/18] Classe que modela as informações que cada cargo do Processo Seletivo deve conter.
    Cada cargo ficará "solto" e deverá ser filtrado depois para as diferentes instancias e tipos de cargo que
    Atributos:
        Instância; (2016, 2015, 2014...)
        Categoria; (Diretor, Coordenador ou Assessor)
        Nome;
        Pertence a; (Diretoria a qual faz parte)
        Requisitos;
        Descrição;
    Métodos:
        __str__
        get_absolute_url
        mais_recente (Pega versão mais recente do PS. Ordenado pela instância e categoria)
    """
    pass
