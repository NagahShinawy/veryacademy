from django.urls import path

from apps.core.views import (
    BooksList,
    DeleteBookView,
    EditBookView,
    OfferBooksView,
    SingleBookView,
)

app_name = "books"

urlpatterns = [
    path("", BooksList.as_view(), name="books_list"),
    path("offers/", OfferBooksView.as_view(), name="offers"),
    path("<int:pk>", SingleBookView.as_view(), name="single"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="delete"),
    path("edit/<int:pk>", EditBookView.as_view(), name="edit"),
]
