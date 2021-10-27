from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteModelForm
from .mixin import PermissionMixin


class NoteIndexView(TemplateView):
    # django template language DTL: allow you to use vars, tags and filters at HTML pages
    # source : https://realpython.com/django-templates-tags-filters/#choosing-a-template-language
    template_name = "home/home.html"
    extra_context = {"username": "John"}
    UNKNOWN_USER = "Unknown"

    @property
    def is_user_authenticated(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        data = super(NoteIndexView, self).get_context_data(**kwargs)
        data["custom_user"] = (
            self.request.user.username.title()
            if self.request.user.is_authenticated
            else self.UNKNOWN_USER
        )
        success_url = reverse_lazy(
            "books:books_list"
        )  # map view name to URL route [path]
        print(success_url)

        return data

    # just test redirect status code
    # def get(self, request, *args, **kwargs):
    #     return redirect("admin:index")


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin/"


class NoteListView(ListView):
    model = Note
    template_name = "home/home.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user, is_active=True)


class NoteDetailsView(PermissionMixin, DetailView):
    model = Note
    context_object_name = "note"
    template_name = "home/note.html"


class CreateNoteView(CreateView):
    model = Note
    fields = ["title", "description", "is_active"]
    template_name = "home/create_note.html"
    success_url = reverse_lazy("home:all")


class CreateNoteBookView(CreateView):
    model = Note
    form_class = NoteModelForm
    template_name = "home/create_note.html"
    success_url = reverse_lazy("home:all")


class UpdateNoteView(PermissionMixin, UpdateView):
    model = Note
    form_class = NoteModelForm
    template_name = "home/create_note.html"

    def get_success_url(self):
        return reverse("home:note", args=(self.object.pk,))


class DeleteNoteView(PermissionMixin, DeleteView):
    model = Note
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("home:all")
    template_name = "home/confirm-delete.html"
    context_object_name = "note"
