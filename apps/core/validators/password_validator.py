import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class BasePasswordValidator:
    message = ""
    code = ""
    REGEX = ""

    def raise_error(self):
        raise ValidationError(_(self.message), self.code)

    def validate(self, password, *arg, **kwargs):
        if not re.findall(self.REGEX, password):
            self.raise_error()

    def get_help_text(self):
        return _(self.message)


class NumberValidator(BasePasswordValidator):
    message = "The password must contain at least 1 digit, 0-9."
    code = "password_no_number"
    REGEX = r"\d"

    def __init__(self, min_digits=1):
        self.min_digits = min_digits


class UppercaseValidator(BasePasswordValidator):
    message = "The password must contain at least 1 uppercase letter, A-Z."
    code = "password_no_upper"
    REGEX = r"[A-Z]"


class LowercaseValidator(BasePasswordValidator):
    message = "The password must contain at least 1 lowercase letter, a-z."
    code = "password_no_lower"
    REGEX = r"[a-z]"


class SymbolValidator(BasePasswordValidator):
    message = r"The password must contain at least 1 symbol: ()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
    code = "password_no_symbol"
    REGEX = r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]"
