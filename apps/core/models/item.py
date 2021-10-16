from django.db import models
from django.contrib.auth.models import User
from apps.core.mixins import (
    InfoModelMixin,
    SlugModelMixin,
    CreatedModelMixin,
    UpdatedModelMixin,
    IsActiveModelMixin,
    PriceModelMixin,
)

from apps.core.managers import ProductManager
from apps.core.constants import NULL_BLANK


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
    PriceModelMixin,
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

    objects = ProductManager()

    class Meta:
        verbose_name_plural = "Store Products"
        verbose_name = "Single Product"
        ordering = ["-created"]


# create db model with 2 fields [ product_ptr_id, pages]
# product_ptr_id: FK
# pages: new field
# كل نوت هو برودكت بس مش شرط كل برودكت يبقى نوت
class NoteBook(Product):
    pages = models.PositiveSmallIntegerField()
