from django.db import models


class Gender(models.TextChoices):
    male = ("male", "Male")
    female = ("female", "Female")