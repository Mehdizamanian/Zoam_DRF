
from rest_framework import serializers
from posts.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Article
        fields=("title","context","author")
        # fields=("__all__")
        # exclude=("status")