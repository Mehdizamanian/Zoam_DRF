"""zoam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from posts.views import index,ArticleList
# from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeTokenApi
from rest_framework_simplejwt import views as jwt_views
app_name="blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    # path('api-auth/', include('rest_framework.urls')),#safe login az tarigh session
    path("Article",ArticleList.as_view(),name="list"),
    path("api/",include("api.urls")),
    # path('api/token-auth/',obtain_auth_token),
    # path("api/revoke/",RevokeTokenApi.as_view()),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
