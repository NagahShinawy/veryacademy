from django.db import models
from apps.core.validators import RangeValidator


class AgeField(models.SmallIntegerField):
    UNDERAGE = 18
    RETIREMENT = 60

    # default_validators = [RangeValidator(UNDERAGE, RETIREMENT)]
