from django.urls import path

from apps.core.views import (
    ProductListView,
    NoteBookListView,
)

app_name = "item"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),
    path("notes/", NoteBookListView.as_view(), name="notes"),
]
