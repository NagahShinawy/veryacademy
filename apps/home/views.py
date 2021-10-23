from django.views.generic.base import TemplateView


class NoteIndexView(TemplateView):
    template_name = "home/home.html"
