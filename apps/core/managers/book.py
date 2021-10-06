from django.db import models


class BookManager(models.Manager):
    def get_offers(self):
        return self.filter(has_offer=True)

    def get_by_author(self, author):
        return self.filter(author=author)
