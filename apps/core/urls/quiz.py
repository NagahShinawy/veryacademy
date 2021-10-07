from django.urls import path
from apps.core.views import QuizAPIView


app_name = "quiz"

urlpatterns = [
    path("quizzes/", QuizAPIView.as_view(), name="books_list"),
    path("categories/", QuizAPIView.as_view(), name="books_list"),
]
