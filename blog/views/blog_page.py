from django.shortcuts import render
from blog.models import Page


# Create your views here.
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
