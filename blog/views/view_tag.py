from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.http import Http404

PER_PAGE = 12


def tag(request, slug):
    post = Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # TAG TITLE
    if len(page_obj) == 0:
        raise Http404()

    filtered_tags = page_obj[0].tags.filter(slug=slug)

    if filtered_tags.exists():  # Verifica se a tag existe
        tag = filtered_tags.first()  # Obtém a primeira tag
        page_title = f"{tag.name} - Tag - "
        page_title_for_tag_page = f"{tag.name}"
    else:
        page_title = f"Posts com a tag '{slug}'"
    # TAG TITLE AND

    context = {
        'page_obj': page_obj,
        'page_title': page_title,
        'page_title_for_tag_page': page_title_for_tag_page,
    }

    return render(
        request,
        'blog/pages/tags.html',
        context
    )
