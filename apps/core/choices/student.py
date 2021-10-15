from django.db import models


class Gender(models.TextChoices):
    MALE = ("m", "Male")
    FEMALE = ("f", "Female")
    NOT_SPECIFIED = ("n", "Not Specified")


class MaritalStatus(models.TextChoices):
    MARRIED = ("married", "Married")
    UNMARRIED = ("unmarried", "Unmarried")
