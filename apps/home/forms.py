from django import forms
from django.core.exceptions import ValidationError
from .models import Note


class NoteModelForm(forms.ModelForm):

    DJANGO = "django"

    class Meta:
        model = Note
        fields = ("title", "description", "is_active")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and self.DJANGO not in title.lower():
            raise ValidationError(f"Missing <{self.DJANGO}> in title")
        return title
