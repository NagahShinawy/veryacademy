from django.conf import settings
from rest_framework import serializers
from apps.core.models import Category, Quizzes


class QuizSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format=settings.QUIZ_DATETIME_FORMAT)

    class Meta:
        model = Quizzes
        fields = [
            "id",
            "title",
            "category",
            "created",
        ]

    def to_representation(self, instance):
        instance.title = instance.title.upper()
        return super().to_representation(instance)


class CategoriesSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "quizzes"]
