from rest_framework import fields
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from django.conf import settings
from apps.lne.models import ContactUs
from apps.lne.errors import NotEgyptPhoneNumber


class NationalIDField(fields.RegexField):
    """ Field representing a National ID """

    NID_REGEX = r"^[12]{1}\d{9}$"
    default_error_messages = {
        "invalid": f"National ID must match the pattern {NID_REGEX}"
    }

    def __init__(self, **kwargs):
        super().__init__(self.NID_REGEX, **kwargs)


class ContactUsSerializers(serializers.ModelSerializer):
    nationalid = NationalIDField()
    phone = PhoneNumberField()

    class Meta:
        model = ContactUs
        fields = "__all__"

    def validate_phone(self, value):
        if value.country_code != settings.EGYPT_CODE_PREFIX:
            raise serializers.ValidationError(NotEgyptPhoneNumber.message)
        return value
