from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.contrib.auth.models import User
from django.http import Http404

PER_PAGE = 12


def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()
    post = Post.objects.get_published().filter(created_by__pk=author_pk)
    # POSTS TITLE
    if user is None:
        raise Http404()
    user_full_name = user.username
    if user.first_name:
        user_full_name = f"{user.first_name} {user.last_name}"
    page_title = 'Posts de ' + user_full_name + ' - '
    # POSTS TITLE AND

    paginator = Paginator(post, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': page_title,
    }

    return render(
        request,
        'blog/pages/created_by.html',
        context,
    )
