from django.urls import path


app_name="blog"

urlpatterns = [

    path("",ArticleList.as_view(),name="list"),

]
