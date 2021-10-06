from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    CreateView,
)

from apps.core.models import Book
from apps.core.choices import BookStatus


class BooksList(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"
    ordering = "-published"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BooksList, self).get_context_data()
        context["offers"] = self.model.objects.filter(has_offer=True)
        return context

    def get_queryset(self):
        return self.model.objects.get_by_author(author=self.request.user)


class SingleBookView(DetailView):
    model = Book
    template_name = "books/book.html"
    context_object_name = "book"
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        book = self.model.objects.get(pk=self.kwargs.get("pk"))
        if book.status == BookStatus.DRAFT:
            raise Http404()
        return book


class DeleteBookView(DeleteView):
    model = Book
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("books:books_list")
    template_name = "books/confirm-delete.html"
    context_object_name = "book"


class EditBookView(UpdateView):
    model = Book
    pk_url_kwarg = "pk"
    template_name = "books/edit.html"
    context_object_name = "book"
    fields = "__all__"

    def get_success_url(self):
        return reverse("books:single", args=(self.object.pk,))


class OfferBooksView(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        return (
            self.model.objects.get_by_author(self.request.user)
            & self.model.objects.get_offers()
        )


class CreateBookView(CreateView):
    model = Book
    template_name = "books/add.html"
    fields = "__all__"
    success_url = reverse_lazy("books:books_list")
