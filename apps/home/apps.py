from importlib import import_module
from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.home"

    def ready(self):
        import_module("apps.home.signals")
