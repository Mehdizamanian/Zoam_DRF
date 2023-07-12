from django.shortcuts import render
from .serializers import ArticleSerializer,UserSerializer
from posts.models import Article
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser ,IsAuthorOrReadOnly,IsStaffOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response



class ArticleListApi(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

# Create your views here.

class ArticleDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

class UserListSerializerApi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetailApi (RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class RevokeTokenApi(APIView):
    permission_classes = (IsAdminUser,)

    def get (self,request):
        return Response({"method":"get"})

    def post (self,request):
        return Response({"ur message":"post"})

    def delete (self,request):
        request.auth.delete()
        return Response({"ur message":"post"},status=401)

    def put (self,request):
        return Response({"method":"put"})