from django.shortcuts import render

from .serializers import ArticleSerializer,UserSerializer
from posts.models import Article
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser


class ArticleListApi(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.

class ArticleDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserListSerializerApi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class UserDetailApi (RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)