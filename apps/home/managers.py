from django.db import models


class NoteManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)
