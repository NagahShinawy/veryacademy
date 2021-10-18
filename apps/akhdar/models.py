from django.db import models
from apps.core.mixins import CreatedModelMixin, InfoModelMixin, EmailModelMixin


class Publisher(EmailModelMixin, models.Model):
    """A company that publishes books."""

    name = models.CharField(
        verbose_name="Name", max_length=50, help_text="The name of the Publisher."
    )
    website = models.URLField(
        verbose_name="Website", help_text="The Publisher's website."
    )


class Book(InfoModelMixin, CreatedModelMixin, models.Model):
    """A published book."""

    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(
        to=Publisher, on_delete=models.PROTECT, related_name="books"
    )

    class Meta:
        verbose_name = "Akhdar Book"


class Contributor(EmailModelMixin, models.Model):
    """
    A contributor to a Book, e.g. author, editor, \
    co-author.
    """

    first_names = models.CharField(
        max_length=50, help_text="The contributor's first name or names."
    )
    last_names = models.CharField(
        max_length=50, help_text="The contributor's last name or names."
    )
