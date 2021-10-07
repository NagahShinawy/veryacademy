from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.serializers import QuizSerializer, CategoriesSerializer
from apps.core.models import Quizzes, Category


class QuizAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
