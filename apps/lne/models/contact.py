from django.db import models


class ContactUs(models.Model):
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

    class Meta:
        verbose_name = "Contact"

    def __str__(self):
        return f"{self.name} - {self.nationalid}"

    name = models.CharField(max_length=256, verbose_name="Name")
    nationalid = models.CharField(max_length=10, verbose_name="National ID")
    phone = models.CharField(max_length=13, verbose_name="Mobile Number")
    reason = models.CharField(
        max_length=20,
        choices=Reason.choices,
        null=True,
        blank=True,
        verbose_name="Reason",
    )
    service = models.CharField(
        max_length=30, choices=Service.choices, verbose_name="Service"
    )

    description = models.TextField(max_length=300)
