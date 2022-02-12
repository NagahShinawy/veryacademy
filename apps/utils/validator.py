from datetime import date

from django.core.exceptions import ValidationError
from .constants import FUTURE_DATE_NOT_ALLOWED


def valid_incorporation_date(value):
    today = date.today()
    if value > today:
        raise ValidationError(FUTURE_DATE_NOT_ALLOWED)
    return value
