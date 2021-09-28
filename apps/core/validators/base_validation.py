from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, BaseValidator


class MinAgeValidator(MinValueValidator):

    message = "Age Must be at least '%(limit_value)d' not '%(show_value)d'"


class MaxAgeValidator(MaxValueValidator):
    message = "Age Must be at Max '%(limit_value)d' not '%(show_value)d'"


class AgeRangeValidator(BaseValidator):
    UNDERAGE = 18
    RETIREMENT = 60
    message = f"Range must in between {UNDERAGE}-{RETIREMENT}"

    def __init__(self, min_value, max_value):
        super().__init__(min_value)
        self.max = max_value

    def clean(self, x):
        if x not in range(self.UNDERAGE, self.RETIREMENT):
            raise ValidationError(self.message)
        return x
