from django.http import Http404
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin


class PermissionMixin(SingleObjectMixin, View):
    def is_note_creator(self, note):
        return self.request.user == note.owner

    def get_object(self, queryset=None):
        note = super().get_object(queryset)
        if not self.is_note_creator(note):
            raise Http404("Note not found")
        return note
