from django.urls import path
from apps.core.views import QuizAPIView, CategoryAPIView


app_name = "quiz"

urlpatterns = [
    path("quizzes/", QuizAPIView.as_view(), name="books_list"),
    path("categories/", CategoryAPIView.as_view(), name="books_list"),
]
