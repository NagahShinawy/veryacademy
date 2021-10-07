from django.urls import path
from apps.core.views import RetrieveQuizAPIView, CategoryAPIView, QuizAPIView


app_name = "quiz"

urlpatterns = [
    path("quizzes/", QuizAPIView.as_view(), name="quizzes"),
    path("quizzes/<int:pk>/", RetrieveQuizAPIView.as_view(), name="retrieve_quizzes"),
    path("categories/", CategoryAPIView.as_view(), name="books_list"),
]
