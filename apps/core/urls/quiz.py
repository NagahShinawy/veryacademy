from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.core.views import (
    CategoryAPIView,
    QuizAPIView,
    RetrieveCategoryAPIView,
    RetrieveQuizAPIView,
    PersonViewSet,
)

app_name = "quiz"

urlpatterns = [
    path("quizzes/", QuizAPIView.as_view(), name="quizzes"),
    path("quizzes/<int:pk>/", RetrieveQuizAPIView.as_view(), name="retrieve_quizzes"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path(
        "categories/<int:pk>",
        RetrieveCategoryAPIView.as_view(),
        name="retrieve_category",
    ),
]


router = DefaultRouter()
router.register("persons", PersonViewSet)

urlpatterns += [path("", include(router.urls))]
