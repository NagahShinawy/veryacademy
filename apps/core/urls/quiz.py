from django.urls import path


app_name = "quiz"

urlpatterns = [
    path("", BooksList.as_view(), name="books_list"),
]
