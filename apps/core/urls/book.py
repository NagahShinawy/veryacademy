from django.urls import path

from apps.core.views import (
    BooksList,
    DeleteBookView,
    EditBookView,
    OfferBooksView,
    SingleBookView,
    CreateBookView,
)

app_name = "books"

urlpatterns = [
    path("", BooksList.as_view(), name="books_list"),
    path("create/", CreateBookView.as_view(), name="create"),
    path("offers/", OfferBooksView.as_view(), name="offers"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="delete"),
    path("edit/<int:pk>", EditBookView.as_view(), name="edit"),
    path("<int:pk>/", SingleBookView.as_view(), name="single"),
]
