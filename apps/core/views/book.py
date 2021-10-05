from django.views.generic import ListView
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
