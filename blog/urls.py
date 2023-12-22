from django.urls import path
from blog.views import index, page, post, projects

app_name = "blog"

urlpatterns = [
    path('', index, name='index'),
    path('page/', page, name='page'),
    path('post/', post, name='post'),
    path('projects/', projects, name='projects'),
]
