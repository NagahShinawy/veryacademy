from django.urls import path

from apps.core.views import (
   ServerListView
)

app_name = "server"

urlpatterns = [
    path("servers/", ServerListView.as_view(), name="servers"),
]
