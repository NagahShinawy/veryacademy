from django.urls import path

from apps.home.views import (
    NoteIndexView,
    AuthorizedView,
    NoteListView,
    NoteDetailsView,
    CreateNoteView,
    CreateNoteBookView
)

app_name = "home"

urlpatterns = [
    path("", NoteIndexView.as_view(), name="notes"),
    path("create/", CreateNoteView.as_view(), name="create"),
    path("create_notebook/", CreateNoteBookView.as_view(), name="create_notebook"),
    path("all/", NoteListView.as_view(), name="all"),
    path("<int:pk>/", NoteDetailsView.as_view(), name="note"),
    path("authorized/", AuthorizedView.as_view(), name="authorized"),
]
