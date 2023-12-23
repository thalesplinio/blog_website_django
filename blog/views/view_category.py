from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.http import Http404

PER_PAGE = 12


def category(request, slug):
    post = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # CATEGORY TITLE
    if len(page_obj) == 0:
        raise Http404()

    page_title = f"{page_obj[0].category.name} - Categoria - "
    print(page_title)
    # CATEGORY TITLE AND

    context = {
        'page_obj': page_obj,
        'page_title': page_title,
    }

    return render(
        request,
        'blog/pages/category.html',
        context,
    )
