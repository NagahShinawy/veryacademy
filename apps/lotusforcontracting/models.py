from django.db import models
from apps.utils.validator import valid_incorporation_date
from .mixins import NameModelMixin
from .managers import DirectorModelManager


class Company(NameModelMixin, models.Model):
    legal_name = models.CharField(max_length=100)
    incorporation_date = models.DateField(validators=[valid_incorporation_date])

    def __str__(self):
        return f"{self.name} - {self.incorporation_date}"


class Director(NameModelMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    objects = DirectorModelManager()

    def delete(self, using=None, keep_parents=False):
        self.end_date = None
        self.save()

    def __str__(self):
        return f"{self.name} - {self.company.name}"
