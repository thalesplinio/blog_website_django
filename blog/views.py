from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page, Technology

PER_PAGE = 12


def index(request):
    # puxando nossos 3 posts mais recentes do index
    posts = Post.objects.filter(is_published=True).order_by("-pk").all()[:3]
    # puxando post em destaque, sempre o mais atualizado
    # posts_destaque = Post.objects.filter(
    #     is_published=True).latest("created_at")
    # puxando tecnologias
    technology = Technology.objects.all()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj,
        # 'posts_destaque': posts_destaque,
        'technology': technology,
    }

    return render(
        request,
        'blog/pages/index.html',
        context,
    )


def page(request):
    page_setup = Page.objects.order_by("-id").first()

    context = {
        'page_setup': page_setup,
    }

    return render(
        request,
        'blog/pages/page.html',
        context,
    )


def post(request, slug):
    # para puxar o post de cada link que clicar
    post = Post.objects.get_published().filter(slug=slug).first()

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
        }
    )


def created_by(request, author_pk):
    post = Post.objects.get_published().filter(created_by__pk=author_pk)

    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/projects.html',
        {
            'page_obj': page_obj,
        }
    )


def category(request, slug):
    post = Post.objects.get_published().filter(category__slug=slug)

    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/projects.html',
        {
            'page_obj': page_obj,
        }
    )


def projects(request):
    # posts = Post.objects.filter(is_published=True).order_by('-pk')
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/projects.html',
        {
            'page_obj': page_obj,
        }
    )
