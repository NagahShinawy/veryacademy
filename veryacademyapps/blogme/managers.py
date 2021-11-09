from django.db import models
from .choices import Option


class PostObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Option.PUBLISHED)
