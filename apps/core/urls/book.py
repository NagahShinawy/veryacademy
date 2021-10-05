from django.urls import path
from apps.core.views import (
    BooksList,
    SingleBookView,

)

app_name = "books"

urlpatterns = [
    path("books/", BooksList.as_view(), name="books_list"),
    path("books/<int:pk>", SingleBookView.as_view(), name="single_book"),
]
