from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.db.models import Q

PER_PAGE = 12


def search(request):
    # GET = HTTP
    # get = dicionário python
    # get("html input name='' ")
    search_value = request.GET.get('search', '').strip()
    post = Post.objects.get_published().filter(
        # Titulo contém search_value OU
        Q(title__icontains=search_value) |
        # Excerto contém search_value OU
        Q(excerpt__icontains=search_value) |
        # Conteudo contém search_value
        Q(content__icontains=search_value)
    )

    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }

    return render(
        request,
        'blog/pages/search.html',
        context
    )
