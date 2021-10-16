from django.views.generic import ListView

from apps.core.models import Product, NoteBook


class ProductListView(ListView):
    model = Product
    template_name = "item/products.html"
    # context_object_name = "products"
    ordering = ["-created"]

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProductListView, self).get_context_data()

        # best performance
        # https://stackoverflow.com/questions/33230540/django-select-related-when-to-use-it
        data["products"] = Product.objects.select_related(
            "seller", "category", "notebook"
        )
        # data["products"] = Product.objects.all()

        return data


class NoteBookListView(ListView):
    model = NoteBook
    template_name = "item/notes.html"
    context_object_name = "notes"
