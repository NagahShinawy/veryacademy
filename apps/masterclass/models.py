from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="publishes"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    has_offer = models.BooleanField(default=False)
    width = models.PositiveIntegerField(default=300)
    height = models.PositiveIntegerField(default=300)
    image = models.ImageField(
        upload_to="photos/", default="", width_field="width", height_field="height"
    )

    def __str__(self):
        return f"{self.title} By {self.creator}"

    class Meta:
        ordering = ["id"]
