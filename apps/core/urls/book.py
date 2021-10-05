from django.urls import path
from apps.core.views import (
    BooksList,
    SingleBookView,
    DeleteBookView,
    EditBookView,
)

app_name = "books"

urlpatterns = [
    path("books/", BooksList.as_view(), name="books_list"),
    path("books/<int:pk>", SingleBookView.as_view(), name="single"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="delete"),
    path("edit/<int:pk>", EditBookView.as_view(), name="edit"),
]
