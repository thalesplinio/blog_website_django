from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Technology


PER_PAGE = 12


def index(request):
    # puxando nossos 3 posts mais recentes do index
    posts = Post.objects.filter(is_published=True).order_by("-pk").all()[:3]
    # puxando post em destaque, sempre o mais atualizado
    # posts_destaque = Post.objects.filter(
    #     is_published=True).latest("created_at")
    posts_destaque = Post.objects.filter(is_published=True).order_by("-pk").all()[:1]
    # puxando tecnologias
    technology = Technology.objects.all()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj,
        'posts_destaque': posts_destaque,
        'technology': technology,
        'page_title': 'Página inicial - ',
    }

    return render(
        request,
        'blog/pages/index.html',
        context,
    )
