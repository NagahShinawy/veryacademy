from django.urls import path
from .views import books, book_details


app_name = "masterclass"

urlpatterns = [
    path("", books, name="books"),
    path("books/<int:pk>", book_details, name="book_details"),
]
