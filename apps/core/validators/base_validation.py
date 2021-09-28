from django.core.validators import MinValueValidator, MaxValueValidator


class MinAgeValidator(MinValueValidator):

    message = "Age Must be at least '%(limit_value)d' not '%(show_value)d'"


class MaxAgeValidator(MaxValueValidator):
    message = "Age Must be at Max '%(limit_value)d' not '%(show_value)d'"
