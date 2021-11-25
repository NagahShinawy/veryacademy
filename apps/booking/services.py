from django import forms
from service_objects.services import Service


class CreateBookingService(Service):
    name = forms.CharField()
    email = forms.EmailField()
    checkin = forms.DateField()
    checkout = forms.DateField()

    def process(self):
        name = self.changed_data["name"]
        email = self.changed_data["email"]
        checkin = self.changed_data["checkin"]
        checkout = self.changed_data["checkout"]
