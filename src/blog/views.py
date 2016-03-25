# Importações do Django
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from urllib.parse import quote_plus
from django.utils import timezone

# Importações do Projeto
from .models import Post
from .forms import PostForm


def post_criar(request):
    """[DLL:2016/03/17] Função criar: cria os posts do blog. Utiliza a mesma página que a função post_editar
    Só é possível criar o post numa página específica e apenas o administrador poderá criar os posts."""

    # Se não for staff ou administrador, gera um erro 404
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    # PostForm pega as informações enviadas pelo usuário.
    # O "or None" serve para carregar o form vazio para o usuário preencher (método padrão é sempre GET)
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instancia = form.save(commit=False)
        #print(form.cleaned_data.get("titulo"))
        instancia.save()

        # Documentação para "Message Framework". É preciso adicionar o código no html também
        # https://docs.djangoproject.com/ja/1.9/ref/contrib/messages/
        messages.success(request, "Publicação criada com sucesso")
        return HttpResponseRedirect(instancia.get_absolute_url())

    return render(request, "blog/post_form.html", locals())


def post_listar(request):
    """[DLL:2016/03/13] Mostra todos as postagens do blog. Não mostra o post inteiro.
    Apenas o administrador poderá ver os posts que estão como rascunho ou que possui a data de publicação no futuro."""

    hoje = timezone.now().date()

    # Queryset com todas as postagens do blog
    queryset_lista = Post.objects.ativa() #.orderby("-timestamp")

    if request.user.is_staff or request.user.is_superuser:
        queryset_lista = Post.objects.all()

    # Pesquisa
    pesquisa = request.GET.get("pesquisa")
    if pesquisa:
        # Q é uma função de pesquisa complexa do django
        # Mais detalhes na documentação: https://docs.djangoproject.com/es/1.9/topics/db/queries/#complex-lookups-with-q-objects
        queryset_lista = queryset_lista.filter(
            Q(titulo__icontains=pesquisa) | # | significa "ou"
            Q(conteudo__icontains=pesquisa) |
            Q(autor__icontains=pesquisa)
            ).distinct() # distint() é um filtro para pegar apenas resultados distintos

    # Paginator é uma função comum do Django, que serve para dividir o conteúdo em páginas. Há também a parte do html.
    # Ela pode ser conferida em: https://docs.djangoproject.com/en/1.9/topics/pagination/
    paginator = Paginator(queryset_lista, 2) # Show 25 contacts per page

    pagina_request_var = 'pagina'
    page = request.GET.get(pagina_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    return render(request, "blog/blog-home-1.html", locals())


def post_detalhar(request, slug):
    """[DLL:2016/03/13] Mostra apenas o post na página.
    Apenas o administrador poderá ver os posts que estão como rascunho ou que possui a data de publicação no futuro."""

    instancia = get_object_or_404(Post, slug=slug)

    # Somente staff e/ou administrador podem ver os posts que estão como rascunho ou que serão publicados no futuro
    if instancia.rascunho or instancia.data_publicacao > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    # String gerada a partir do conteudo para compartilhar um post (Para Twitter e Linkedin pricipalmente)
    share_string = quote_plus(instancia.conteudo)

    return render(request, "blog/blog-post.html", locals())


def post_editar(request, slug):
    """[DLL:2016/03/17] Função editar: edita os posts do blog. Utiliza a mesma página que a função post_criar
    Só é possível editar o post numa página específica e apenas o administrador poderá editar os posts."""

    # Se não for staff ou administrador, gera um erro 404
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    # Pega as informações do Post que contém esta slug
    instancia = get_object_or_404(Post, slug=slug)

    # Pega as informações e arquivos enviados ou carrega no forms com as informações pré-existentes
    form = PostForm(request.POST or None, request.FILES or None, instance=instancia)

    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()

        # Documentação para "Message Framework". É preciso adicionar o código no html também
        # https://docs.djangoproject.com/ja/1.9/ref/contrib/messages/
        messages.success(request, "Publicação editada com sucesso")

        return HttpResponseRedirect(instancia.get_absolute_url())

    return render(request, "blog/post_form.html", locals())


def post_deletar(request, slug):
    """[DLL:2016/03/17] Função deletar: apaga os posts do blog.
    Só é possível apagar um de cada vez e apenas o administrador poderá deletar os posts."""

    # Somente os usuários com privilégios de administrador podem acessar essa função
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instancia = get_object_or_404(Post, slug=slug)
    instancia.delete()
    messages.success(request, "Deletado com sucesso")
    return redirect("blog:listar")
