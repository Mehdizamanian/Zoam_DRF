
from django.urls import path,include
from .views import ArticleListApi,ArticleDetailApi,UserListSerializerApi,UserDetailApi

api_name="api"

urlpatterns = [
    path("",ArticleListApi.as_view() , name="list"),
    path("<int:pk>",ArticleDetailApi.as_view() , name="detail"),
    path("users/",UserListSerializerApi.as_view(),name="users"),
    path("users/<int:pk>/",UserDetailApi.as_view(),name="users"),
]