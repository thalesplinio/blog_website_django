from django.shortcuts import render
from blog.models import Post
from django.http import Http404

PER_PAGE = 12


def post(request, slug):
    # para puxar o post de cada link que clicar
    post = Post.objects.get_published().filter(slug=slug).first()

    if post is None:
        raise Http404()

    page_title = f"{post.title} - Post - "

    context = {
        'post': post,
        'page_title': page_title,

    }

    return render(
        request,
        'blog/pages/post.html',
        context,
    )
