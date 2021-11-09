from rest_framework import serializers
from ..blogme.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "author", "excerpt", "content", "status")
        model = Article
