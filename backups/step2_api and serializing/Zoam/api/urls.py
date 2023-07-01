
from django.urls import path,include
from .views import ArticleListApi

api_name="api"

urlpatterns = [
    path("",ArticleListApi.as_view()),

]