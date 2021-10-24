from django.views.generic.base import TemplateView
from django.shortcuts import redirect


class NoteIndexView(TemplateView):
    # django template language DTL: allow you to use vars, tags and filters at HTML pages
    # source : https://realpython.com/django-templates-tags-filters/#choosing-a-template-language
    template_name = "home/home.html"
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
        if self.is_user_authenticated:
            data["notes"] = ["django", "html", "css", "js", "react"]
        return data

    # just test redirect status code
    # def get(self, request, *args, **kwargs):
    #     return redirect("admin:index")
