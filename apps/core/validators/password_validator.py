import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from apps.core.mixins import (
    NumberPatternMixin,
    UpperCasePatternMixin,
    LowerCasePatternMixin,
    SymbolPatternMixin,
    MissingNumberMessage,
    MissingUpperMessage,
    MissingLowerMessage,
    MissingSymbolMessage,
)


class NumberValidator(NumberPatternMixin):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _(MissingNumberMessage.message), code=MissingNumberMessage.code,
            )

    def get_help_text(self):
        return _(MissingNumberMessage.message)


class UppercaseValidator(UpperCasePatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _(MissingUpperMessage.message), code=MissingUpperMessage.code,
            )

    def get_help_text(self):
        return _(MissingUpperMessage.message)


class LowercaseValidator(LowerCasePatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                _(MissingLowerMessage.message), code=MissingLowerMessage.code,
            )

    def get_help_text(self):
        return _(MissingLowerMessage.message)


class SymbolValidator(SymbolPatternMixin):
    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            raise ValidationError(
                MissingSymbolMessage.message, code=MissingSymbolMessage.code,
            )

    def get_help_text(self):
        return _(MissingSymbolMessage.message)
