from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, BaseValidator


class MinAgeValidator(MinValueValidator):

    message = "Age Must be at least '%(limit_value)d' not '%(show_value)d'"


class MaxAgeValidator(MaxValueValidator):
    message = "Age Must be at Max '%(limit_value)d' not '%(show_value)d'"


class RangeValidator(BaseValidator):

    def __init__(self, limit_value, max_value, msg=""):
        super().__init__(limit_value)
        self.max_value = max_value
        if msg:
            self.message = msg
        else:
            self.message = f"Range must in between {limit_value}-{max_value}"

    def clean(self, x):
        if x not in range(self.limit_value, self.max_value):
            raise ValidationError(self.message)
        return x
