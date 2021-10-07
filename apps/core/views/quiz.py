from rest_framework import generics
from apps.core.serializers import QuizSerializer, CategoriesSerializer
from apps.core.models import Quizzes, Category


class QuizAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


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
