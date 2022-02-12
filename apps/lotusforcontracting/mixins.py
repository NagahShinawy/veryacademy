from django.db import models


class NameModelMixin(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
