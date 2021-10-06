from django.db import models


class BookManager(models.Manager):
    def get_offers(self):
        return self.filter(has_offer=True)
