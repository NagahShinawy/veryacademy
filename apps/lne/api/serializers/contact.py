from rest_framework import fields
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from django.conf import settings
from apps.lne.models import ContactUs
from apps.lne.errors import NotEgyptPhoneNumber
from apps.lne.api import constants


class NationalIDField(fields.RegexField):
    """ Field representing a National ID """

    NID_REGEX = r"^[12]{1}\d{9}$"
    default_error_messages = {
        "invalid": f"National ID must match the pattern {NID_REGEX}"
    }

    def __init__(self, **kwargs):
        super().__init__(self.NID_REGEX, **kwargs)


class CustomPhoneNumberField(PhoneNumberField):
    def to_internal_value(self, data):
        phone = super().to_internal_value(data)
        if phone.country_code != settings.EGYPT_CODE_PREFIX:
            raise serializers.ValidationError(NotEgyptPhoneNumber.message)
        return phone


class ContactUsSerializers(serializers.ModelSerializer):
    nationalid = NationalIDField()
    phone = CustomPhoneNumberField()
    NO_BLANK_FIELDS = ["name", "phone", "nationalid"]

    class Meta:
        model = ContactUs
        fields = "__all__"

    # custom error messages, change error message
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.NO_BLANK_FIELDS:
            self.fields[field].error_messages["required"] = constants.NO_BLANK.format(
                field=field
            )
