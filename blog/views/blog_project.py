from django.shortcuts import render


# Create your views here.
def projects(request):
    return render(
        request,
        'blog/pages/projects.html'
    )
