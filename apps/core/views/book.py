from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from apps.core.models import Book


class BooksList(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"
    ordering = "-published"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BooksList, self).get_context_data()
        context["offers"] = self.model.objects.filter(has_offer=True)
        return context


class SingleBookView(DetailView):
    model = Book
    template_name = "books/book.html"
    context_object_name = "book"
    pk_url_kwarg = "pk"


class DeleteBookView(DeleteView):
    model = Book
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("books:books_list")
    template_name = "books/confirm-delete.html"
    context_object_name = "book"
