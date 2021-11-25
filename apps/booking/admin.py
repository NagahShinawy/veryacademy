# list_display django foreign key
# https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field

# custom admin panel
# relationship list display

from django.contrib import admin
from .models import Booking, Customer


@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ("id", "name", "email")


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ("id", "get_name", "get_email", "checkin", "checkout")

    @admin.display(description="name")
    def get_name(self, booking):
        return booking.customer.name

    @admin.display(description="email")
    def get_email(self, booking):
        return booking.customer.email
