from django.views.generic.base import TemplateView


class NoteIndexView(TemplateView):
    template_name = "home/home.html"
    DEFAULT_USER = "lovely user"

    def get_context_data(self, **kwargs):
        data = super(NoteIndexView, self).get_context_data(**kwargs)
        data["welcome"] = (
            self.request.user.username.title()
            if self.request.user.is_authenticated
            else self.DEFAULT_USER
        )
        return data
