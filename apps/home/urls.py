from django.urls import path

from apps.home.views import (
    NoteIndexView,
    AuthorizedView,
    NoteListView,
    NoteDetailsView,
)

app_name = "home"

urlpatterns = [
    path("", NoteIndexView.as_view(), name="notes"),
    path("all/", NoteListView.as_view(), name="all"),
    path("<int:pk>/", NoteDetailsView.as_view(), name="note"),
    path("authorized/", AuthorizedView.as_view(), name="authorized"),
]
