from django.urls import path
from .views import books


app_name = "masterclass"

urlpatterns = [
    path("", books, name="books"),
]
