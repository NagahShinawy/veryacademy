from django.db import models
from django.contrib.auth.models import User
from apps.core.mixins import (
    InfoModelMixin,
    SlugModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
)


class Group(
    InfoModelMixin, CreatedModelMixin, UpdatedModelMixin, SlugModelMixin, models.Model
):
    """
    category group
    """

    class Meta:
        verbose_name = "Group"


class Product(
    InfoModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    SlugModelMixin,
    IsActiveModelMixin,
    models.Model,
):
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Store Products"
        verbose_name = "Single Product"
