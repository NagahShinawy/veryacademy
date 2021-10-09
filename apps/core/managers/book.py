from django.db import models


class BookManager(models.Manager):
    def get_offers(self):
        return self.filter(has_offer=True)

    def get_by_author(self, author):
        return self.filter(author=author)

    def get_by_status(self, status):
        return self.filter(status__iexact=status)


class MedicalItemManager(models.Manager):
    EGYPT = "egypt"

    def get_queryset(self):
        return super().get_queryset().exclude(country__iexact=self.EGYPT)
