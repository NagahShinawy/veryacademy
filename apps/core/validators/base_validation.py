from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator


class RangeValidator(MinValueValidator):
    message = "Range must in between {limit_value}-{max_value} not {value}"

    def __init__(self, limit_value, max_value):
        super().__init__(limit_value)
        self.max_value = max_value

    def error_message(self, value=None):
        return self.message.format(
            limit_value=self.limit_value, max_value=self.max_value, value=value
        )

    def clean(self, x):
        value = super().clean(x)
        if value not in range(self.limit_value, self.max_value + 1):
            raise ValidationError(self.error_message(value))
        return value


class NationalIDValidator(RegexValidator):
    regex = r"^\d{14}$"
    EXACT_DIGITS = 14
    message = "national id must be {exact_digits} digits not {value} digits"

    def __call__(self, value):
        self.message = self.message.format(
            exact_digits=self.EXACT_DIGITS, value=len(str(value))
        )
        super(NationalIDValidator, self).__call__(value)


national_id_validator = NationalIDValidator()
