from django.db import models


class Gender(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")


class MaritalStatus(models.TextChoices):
    MARRIED = ("married", "Married")
    UNMARRIED = ("unmarried", "Unmarried")
