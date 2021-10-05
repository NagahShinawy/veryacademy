from django.urls import path
from apps.core.views import (
    BooksList,
    SingleBookView,
    DeleteBookView,

)

app_name = "books"

urlpatterns = [
    path("books/", BooksList.as_view(), name="books_list"),
    path("books/<int:pk>", SingleBookView.as_view(), name="single_book"),
    path("delete_book/<int:pk>", DeleteBookView.as_view(), name="delete_book"),
]
