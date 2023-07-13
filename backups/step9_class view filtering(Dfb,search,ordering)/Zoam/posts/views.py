from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import ListView


def index (request):
    return HttpResponse('<h1> Welcome </h1>')


class ArticleList(ListView):
    queryset = Article.objects.all()
    context_object_name ='posts'
    template_name = 'blog/article_list.html'


# Create your views here.
