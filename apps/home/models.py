from django.db import models
from apps.core.mixins import (
    InfoModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
)


class Note(
    InfoModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
    models.Model,
):
    """

    """

    class Meta:
        ordering = ["id"]
