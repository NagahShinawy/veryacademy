from django.db import models


class Option(models.TextChoices):
    DRAFT = ("draft", "Draft")
    PUBLISHED = ("published", "Published")
