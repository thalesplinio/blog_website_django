from django.shortcuts import render


# Create your views here.
def page(request):
    return render(
        request,
        'blog/pages/page.html'
    )