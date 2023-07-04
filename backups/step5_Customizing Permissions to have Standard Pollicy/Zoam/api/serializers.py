
from rest_framework import serializers
from posts.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Article
        fields=("title","context","author")
        # fields=("__all__")
        # exclude=("status")

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ("__all__")


