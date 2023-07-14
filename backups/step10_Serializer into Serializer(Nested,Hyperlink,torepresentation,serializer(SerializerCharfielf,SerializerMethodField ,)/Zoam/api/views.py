from django.shortcuts import render
from .serializers import ArticleSerializer,UserSerializer
from posts.models import Article
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser ,IsAuthorOrReadOnly,IsStaffOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# from rest_framework.generics import RetrieveAPIView
# from .serializers import AuthorSerializer

# class ArticleListApi(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)
#
# class ArticleDetailApi(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

class ArticleViewSetApi(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["status",]
    search_fields = ["title", "author", "context"]
    ordering_fields=["pk","status"]
    ordering=["-pk"]

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     return queryset

    def get_permissions(self):

        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]



# class UserListSerializerApi(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser,)
#
# class UserDetailApi (RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser,)

class UserViewSetApi(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

# class RevokeTokenApi(APIView):
#     permission_classes = (IsAdminUser,)
#
#     def get (self,request):
#         return Response({"method":"get"})
#
#     def post (self,request):
#         return Response({"ur message":"post"})
#
#     def delete (self,request):
#         request.auth.delete()
#         return Response({"ur message":"post"},status=401)
#
#     def put (self,request):
#         return Response({"method":"put"})

# class AuthorSerializerapi(RetrieveAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = AuthorSerializer