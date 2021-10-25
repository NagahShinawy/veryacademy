from django.urls import path

from apps.home.views import (
    NoteIndexView,
    AuthorizedView
)

app_name = "home"

urlpatterns = [
    path("", NoteIndexView.as_view(), name="notes"),
    path("authorized/", AuthorizedView.as_view(), name="authorized"),
]
