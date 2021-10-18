from rest_framework.generics import CreateAPIView

from apps.lne.api.serializers import ContactUsSerializers


class ContactUsCreateAPIView(CreateAPIView):
    serializer_class = ContactUsSerializers
