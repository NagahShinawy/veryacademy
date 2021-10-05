from django.urls import path
from apps.core.views import (
    BooksList,
)

app_name = "books"

urlpatterns = [
    path("books/", BooksList.as_view(), name="books_list"),
]
