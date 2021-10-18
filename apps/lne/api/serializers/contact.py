from rest_framework import serializers
from apps.lne.models import ContactUs


class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
