from django.db import models


class Status(models.TextChoices):
    DRAFT = (
        "draft",
        "Draft",
    )
    PUBLISHED = ("published", "Published")
