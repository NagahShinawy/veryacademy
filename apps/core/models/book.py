from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):

    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    has_offer = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("books:single_book", args=[self.pk])

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title
