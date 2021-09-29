from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class RangeValidator(MinValueValidator):
    def __init__(self, limit_value, max_value, msg=""):
        super().__init__(limit_value)
        self.max_value = max_value
        if msg:
            self.message = msg
        else:
            self.message = "Range must in between {limit_value}-{max_value} not {value}"

    def clean(self, x):
        value = super().clean(x)
        if value not in range(self.limit_value, self.max_value + 1):
            raise ValidationError(
                self.message.format(
                    limit_value=self.limit_value, max_value=self.max_value, value=value
                )
            )
        return value
