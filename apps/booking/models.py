from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Booking(models.Model):
    class Status(models.TextChoices):
        NEW = ("new", "New")
        PENDING = ("pending", "Pending")
        ACTIVE = ("active", "Active")
        CANCELED = ("canceled", "Canceled")

    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    checkin = models.DateField(verbose_name="Checkin Date")
    checkout = models.DateField(verbose_name="Checkout Date")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return f"{self.customer.name} {self.checkin}-{self.checkout}"
