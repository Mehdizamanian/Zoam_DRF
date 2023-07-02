
from django.urls import path,include
from .views import ArticleListApi,ArticleDetailApi

api_name="api"

urlpatterns = [
    path("",ArticleListApi.as_view() , name="list"),
    path("<int:pk>",ArticleDetailApi.as_view() , name="detail"),
]