from django.db import models


class Reason(models.TextChoices):
    COMPLAIN = ("complain", "Complain")
    SUGGESTION = ("suggestion", "Suggestion")
    ASKING = ("asking", "Asking")


class Service(models.TextChoices):
    PATIENT = ("patient", "Patient")
    DEPENDANTS = ("dependants", "Dependants")
    COVID = ("covid", "Covid")
    SICK_LEAVE = ("sick leave", "Sick Leave")
    MEDICATION = ("medication", "Medication")
    OTHER = ("other", "Other")


class Status(models.TextChoices):
    SINGLE = ("single", "Single")
    MARRIED = ("married", "Married")