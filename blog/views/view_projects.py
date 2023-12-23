from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post

PER_PAGE = 12


def projects(request):
    # posts = Post.objects.filter(is_published=True).order_by('-pk')
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': 'Home - ',
    }

    return render(
        request,
        'blog/pages/projects.html',
        context,
    )
