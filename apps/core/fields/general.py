from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.validators import RangeValidator


class AgeField(models.SmallIntegerField):
    UNDERAGE = 18
    RETIREMENT = 60

    # default_validators = [RangeValidator(UNDERAGE, RETIREMENT)]


class UpdatedMixin(models.Model):

    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True
