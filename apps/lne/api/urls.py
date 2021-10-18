from django.urls import path
from .views import ContactUsCreateAPIView

app_name = "lns_api"


urlpatterns = [
    path("contact_us/", ContactUsCreateAPIView.as_view(), name="contact_us"),
]
