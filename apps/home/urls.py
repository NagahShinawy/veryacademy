from django.urls import path

from apps.home.views import (
    NoteIndexView,
    AuthorizedView,
    NoteListView,
    NoteDetailsView,
    CreateNoteView,
    CreateNoteBookView,
    UpdateNoteView,
    DeleteNoteView,
    LoginInterfaceView,
    LogoutInterfaceView,
    SignupInterfaceView,
)

app_name = "home"

urlpatterns = [
    path("", NoteIndexView.as_view(), name="notes"),
    path("create/", CreateNoteView.as_view(), name="create"),
    path("create_notebook/", CreateNoteBookView.as_view(), name="create_notebook"),
    path("update/<int:pk>", UpdateNoteView.as_view(), name="update"),
    path("delete/<int:pk>", DeleteNoteView.as_view(), name="delete"),
    path("all/", NoteListView.as_view(), name="all"),
    path("<int:pk>/", NoteDetailsView.as_view(), name="note"),
    path("authorized/", AuthorizedView.as_view(), name="authorized"),
    path("signup/", SignupInterfaceView.as_view(), name="signup"),
    path("login/", LoginInterfaceView.as_view(), name="login"),
    path("logout/", LogoutInterfaceView.as_view(), name="logout"),
]
