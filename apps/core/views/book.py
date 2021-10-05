from django.views.generic import ListView
from apps.core.models import Book


class BooksList(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'
    ordering = '-published'

