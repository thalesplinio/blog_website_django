from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page

PER_PAGE = 12


# Create your views here.
def index(request):
    posts = Post.objects.filter(is_published=True).order_by("-pk").all()[:3]

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    posts_destaque = Post.objects.filter(is_published=True).latest("created_at")

    context = {
        'posts': posts,
        'page_obj': page_obj,
        'posts_destaque': posts_destaque,
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
