from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.validators import RangeValidator
from apps.core.validators import national_id_validator


class AgeField(models.SmallIntegerField):
    UNDERAGE = 18
    RETIREMENT = 60

    default_validators = [RangeValidator(UNDERAGE, RETIREMENT)]


class UpdatedMixin(models.Model):

    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class NationalIDField(models.CharField):

    ID_MAX_DIGITS = 14
    ID_EXAMPLE = "11223344556677"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = self.ID_MAX_DIGITS
        kwargs["validators"] = [
            national_id_validator,
        ]
        kwargs["default"] = self.ID_EXAMPLE

        super(NationalIDField, self).__init__(*args, **kwargs)