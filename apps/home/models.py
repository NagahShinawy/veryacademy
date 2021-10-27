from django.db import models
from apps.core.mixins import (
    InfoModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
)

from .managers import NoteManager


class Note(
    InfoModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
    models.Model,
):
    """

    """

    objects = NoteManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
