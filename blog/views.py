from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page, Technology

PER_PAGE = 12


# Create your views here.
def index(request):
    # puxando nossos 3 posts mais recentes do index
    posts = Post.objects.filter(is_published=True).order_by("-pk").all()[:3]
    # puxando post em destaque, sempre o mais atualizado
    posts_destaque = Post.objects.filter(is_published=True).latest("created_at")
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
    }

    return render(
        request,
        'blog/pages/index.html',
        context,
    )


# Create your views here.
def page(request):
    page_setup = Page.objects.order_by("-id").first()

    print(page_setup.phone)

    context = {
        'page_setup': page_setup,
    }

    return render(
        request,
        'blog/pages/page.html',
        context,
    )


# Create your views here.
def post(request):
    return render(
        request,
        'blog/pages/post.html',
    )


# Create your views here.
def projects(request):
    posts = Post.objects.filter(is_published=True).order_by('-pk')

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
