
from django.urls import path,include
# from .views import ArticleListApi,ArticleDetailApi,UserListSerializerApi,UserDetailApi
from .views import ArticleViewSetApi,UserViewSetApi
from rest_framework import routers

api_name="api"

router = routers.SimpleRouter()
router.register('users',UserViewSetApi,basename="users")
router.register('articles', ArticleViewSetApi,basename="articles")
# urlpatterns = router.urls
urlpatterns=[
    path("",include(router.urls)),
    # path("author/<int:pk>/",AuthorSerializerapi.as_view(),name="author-detail"),
]



# urlpatterns = [
#     path("",ArticleListApi.as_view() , name="list"),
#     path("<int:pk>",ArticleDetailApi.as_view() , name="detail"),
#     path("users/",UserListSerializerApi.as_view(),name="users"),
#     path("users/<int:pk>/",UserDetailApi.as_view(),name="users"),
#
# ]