from django.db import models
from datetime import datetime


class PostManager(models.Manager):

    current_year = datetime.now().year
    last_year = current_year - 1

    def get_by_current_year(self):
        return self.filter(published__year=self.current_year)

    def get_by_last_year(self):
        return super().get_queryset().filter(publish__year=self.last_year)

    def get_queryset(self):
        return self.get_by_last_year()
