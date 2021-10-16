from django.views.generic import ListView

from apps.core.models import Product, NoteBook


class ProductListView(ListView):
    model = Product
    template_name = "item/products.html"
    context_object_name = "products"


class NoteBookListView(ListView):
    model = NoteBook
    template_name = "item/notes.html"
    context_object_name = "notes"
