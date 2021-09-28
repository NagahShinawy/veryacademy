from django.db import models
from apps.core.validators import MinAgeValidator, MaxAgeValidator


class AgeField(models.SmallIntegerField):
    UNDERAGE = 18
    RETIREMENT = 60

    def __init__(self, **kwargs):
        kwargs["validators"] = [MinAgeValidator(AgeField.UNDERAGE), MaxAgeValidator(AgeField.RETIREMENT)]
        super(AgeField, self).__init__(**kwargs)

