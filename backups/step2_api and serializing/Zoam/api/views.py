from django.shortcuts import render

from .serializers import ArticleSerializer
from posts.models import Article
from rest_framework.generics import ListCreateAPIView


class ArticleListApi(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
# Create your views here.
