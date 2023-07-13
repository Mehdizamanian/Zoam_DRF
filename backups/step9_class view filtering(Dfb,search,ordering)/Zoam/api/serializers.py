
from rest_framework import serializers
from posts.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Article
        fields=("title","context","author")
        # fields=("__all__")
        # exclude=("status")

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ("__all__")


