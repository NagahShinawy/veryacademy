from django.urls import path

from apps.home.views import (
    NoteIndexView,
)

app_name = "home"

urlpatterns = [
    path("", NoteIndexView.as_view(), name="notes"),
]
