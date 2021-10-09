from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.core.managers import BookManager
from apps.core.choices import BookStatus
from apps.core.mixins import TimeStampModelMixin, InfoModelMixin, GenderModelMixin, NationalIDField


class Author(InfoModelMixin, GenderModelMixin, TimeStampModelMixin, models.Model):
    """
    author model implement abstract model classes
    """
    national_id = NationalIDField()


class Book(models.Model):

    SINGLE_VIEW_NAME = "books:single"
    DELETE_VIEW_NAME = "books:delete"
    UPDATE_VIEW_NAME = "books:update"

    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=BookStatus.choices, default=BookStatus.DRAFT
    )
    has_offer = models.BooleanField(default=False)

    objects = BookManager()

    def get_absolute_url(self):
        return reverse(self.SINGLE_VIEW_NAME, args=[self.pk])

    @property
    def delete_url(self):
        return reverse(self.DELETE_VIEW_NAME, args=[self.pk])

    @property
    def update_url(self):
        return reverse(self.UPDATE_VIEW_NAME, args=[self.pk])

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title
