import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from apps.core.mixins import (
    NumberPatternMixin,
    UpperCasePatternMixin,
    LowerCasePatternMixin,
    SymbolPatternMixin,
)


class NumberValidator(NumberPatternMixin):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code="password_no_number",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")


class UppercaseValidator(UpperCasePatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="password_no_upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class LowercaseValidator(LowerCasePatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code="password_no_lower",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 lowercase letter, a-z.")


class SymbolValidator(SymbolPatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _(
                    "The password must contain at least 1 symbol: "
                    + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
                ),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: "
            + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
