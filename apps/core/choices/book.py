from django.db import models


class BookStatus(models.TextChoices):

    PUBLISHED = ("published", "Published")
    DRAFT = ("draft", "Draft")
