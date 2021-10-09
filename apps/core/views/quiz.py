from rest_framework import generics

from apps.core.models import Category, Quizzes
from apps.core.pagination import CategoryPagination, QuizPagination
from apps.core.serializers import CategoriesSerializer, QuizSerializer


class QuizAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
    pagination_class = QuizPagination


class RetrieveQuizAPIView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    lookup_url_kwarg = "pk"

    def get_object(self):
        quiz = Quizzes.objects.get(pk=self.kwargs.get("pk"))
        return quiz

    # def get_queryset(self):
    #     return Quizzes.objects.filter(pk=self.kwargs.get("pk"))


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination


class RetrieveCategoryAPIView(RetrieveQuizAPIView):
    serializer_class = CategoriesSerializer

    def get_object(self):
        return Category.objects.get(pk=self.kwargs.get("pk"))
