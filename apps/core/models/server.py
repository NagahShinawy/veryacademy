from django.db import models
from apps.core.constants import NULL_BLANK


class BaseSever(models.Model):
    hardware = models.CharField(max_length=256, **NULL_BLANK)
    os = models.CharField(max_length=50, **NULL_BLANK)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.hardware} {self.os}"

    @property
    def is_exist(self):
        return self.hardware and self.os


class Server(BaseSever):
    pass


class Ubuntu(BaseSever):
    version = models.CharField(max_length=10, **NULL_BLANK)


class Centos(BaseSever):
    class Release(models.TextChoices):
        SHORT = ("short", "Short")
        LONG = ("long", "Long")

    release = models.CharField(
        max_length=10, choices=Release.choices, default=Release.SHORT
    )
