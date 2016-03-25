# Importações do Django
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone


class PostManager(models.Manager):
    """[DLL:2016/03/14] Esta classe sobrescreve o valor padrão de all [Post.objects.all()]"""
    def ativa(self, *args, **kwargs):
        """[DLL:2016/03/14] O método ativa filtra todos os posts que não estão marcados como rascunho e não possuem """
        # super(PostManager, self).all() -> Post.objects.all()
        return super(PostManager, self).filter(rascunho=False).filter(data_publicacao__lte=timezone.now())


def upload_location(instancia, nome_arquivo):
    """[DLL:2016/03/14] Função para mostrar o caminho onde a upload da mídia será feito.
    No caso, cria uma pasta com o nome do objeto e coloca o arquivo dentro."""
    return "%s/%s" % (instancia.id, nome_arquivo)

class Post(models.Model):
    """[DLL:2016/03/12] Classe que modela as informações que cada Post no blog deve conter.
    Atributos:
        Título do post;
        Autor;
        Conteúdo;
        Imagem;
        Data de Criação;
        Rascunho;
        Data de Publicação;
        Última Atualização;
    Métodos:
        __str__
        get_absolute_url
    """
    # Para mais informações sobre os diferentes Fields, visite: https://docs.djangoproject.com/en/1.9/ref/models/fields/
    titulo = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)
    conteudo = models.TextField()
    rascunho = models.BooleanField(default=False)
    data_publicacao = models.DateField(auto_now=False, auto_now_add=False)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Cria uma slug que deve ser única para cada objeto dessa classe
    slug = models.SlugField(unique=True)

    # ImageField precisa do Pillow (pacote do Python de renderização de imagens) instalado
    imagem = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="comprimento_imagem",
            height_field="altura_imagem")

    altura_imagem = models.IntegerField(default=0)
    comprimento_imagem = models.IntegerField(default=0)

    # Este "objects" se refere ao usado em locais como: Post.objects.all()
    objects = PostManager()

    # A classe Meta serve para tudo que não é um atributo ou método. Apenas para "descrever" a classe melhor
    class Meta:
        ordering = ["-id", "-data_criacao", "-ultima_atualizacao"]


    def __str__(self):
        """Ao chamar um objeto da classe em forma de string, este atributo será retornado"""
        return self.titulo

    def get_absolute_url(self):
        return reverse("blog:detalhar", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    """[DLL:2016/03/14] Função recursiva que cria um slug único para ser usado no url"""

    # Transforma o título em uma slug
    slug = slugify(instance.titulo)

    # Só usado caso a função esteja sendo chamada pela segunda vez (ou mais).
    if new_slug is not None:
        slug = new_slug

    # Filtra os slugs dos objetos da classe Post e verifica se já existe algum com o mesmo slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    # Verifica se a slug já existe e chama a função de novo caso ocorra
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    # Caso a slug seja única, retorna a slug
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """[DLL:2016/03/14] Verifica se a instância possui uma slug e cria caso necessário.
    *args e **kwargs pegam os outros parâmetros que a função exige"""
    if not instance.slug:
        instance.slug = create_slug(instance)

# Cria a slug a partir da string gerada pela função pre_save_post_receiver
pre_save.connect(pre_save_post_receiver, sender=Post)
