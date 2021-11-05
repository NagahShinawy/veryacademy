from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="publishes"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} By {self.creator}"
