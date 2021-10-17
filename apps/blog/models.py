from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.core.mixins import (
    UpdatedModelMixin,
    CreatedModelMixin,
    SlugModelMixin,
    InfoModelMixin,
)
from .choices import Status
from .managers import PostManager


class Post(InfoModelMixin, CreatedModelMixin, UpdatedModelMixin, models.Model):
    EMPTY = ""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    publish = models.DateTimeField(default=timezone.now)

    # unique slug for the same date [ you can not create the same slug at the same date ]
    slug = models.SlugField(unique_for_date="publish", default=EMPTY)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )

    objects = PostManager()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.title
