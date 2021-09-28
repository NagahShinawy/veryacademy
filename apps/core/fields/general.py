from django.db import models
from apps.core.validators import AgeRangeValidator


class AgeField(models.SmallIntegerField):
    UNDERAGE = 18
    RETIREMENT = 60

    default_validators = [AgeRangeValidator(UNDERAGE, RETIREMENT)]



