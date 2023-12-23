from django.shortcuts import render
from blog.models import Page
from django.http import Http404

PER_PAGE = 12


def page(request):
    page_setup = Page.objects.order_by("-id").first()
    # Busca do full_name da pagina
    page = Page.objects.first()

    if page is None:
        raise Http404()

    page_title = f"{page.full_name} - Sobre min - "

    context = {
        'page_setup': page_setup,
        'page_title': page_title,
    }

    return render(
        request,
        'blog/pages/page.html',
        context,
    )
