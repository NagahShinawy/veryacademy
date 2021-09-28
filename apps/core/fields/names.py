from django.core.validators import RegexValidator
from django.db.models import CharField
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


class PatternBase:

    DASH = "\-"  # pylint: disable=anomalous-backslash-in-string
    SPACE = "\s"  # pylint: disable=anomalous-backslash-in-string


class ArabicPattern(PatternBase):
    LETTERS = (
        "\u0621-\u063A\u0641-\u064A\ufbe8-\ufbef\ufbfb-\ufc5a"
        "\ufc5e-\ufcd8\ufcda-\ufcf1\ufcf5-\ufdc7\ufe80-\ufefc"
    )
    NUMBERS = "\u0660-\u0669"


class EnglishPattern(PatternBase):
    LETTERS = "A-Za-z"
    NUMBERS = "0-9"


class BaseUnicodeField(CharField):
    patterns = set()

    def _build_pattern(self):
        if not isinstance(self.patterns, set):
            raise TypeError("Patterns should be a set")
        return "^[" + "".join(self.patterns) + "]+$"

    @cached_property
    def validators(self):
        validators = super().validators
        regex_validator = RegexValidator(self._build_pattern())
        validators.append(regex_validator)
        return validators


class ArabicNameField(BaseUnicodeField):
    patterns = {ArabicPattern.LETTERS, ArabicPattern.SPACE, ArabicPattern.DASH}
    default_error_messages = {
        "invalid": _(
            "Value should consist only of Arabic letters, spaces and/or dashes."
        )
    }


class EnglishNameField(BaseUnicodeField):
    patterns = {EnglishPattern.LETTERS, EnglishPattern.SPACE, EnglishPattern.DASH}
    default_error_messages = {
        "invalid": _(
            "Value should consist only of English letters, spaces and/or dashes."
        )
    }
