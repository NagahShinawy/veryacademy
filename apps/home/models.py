from django.contrib.auth.models import User
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

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes", null=True, blank=True
    )
    objects = NoteManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
