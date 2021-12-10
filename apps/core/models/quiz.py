from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]

    title = models.CharField(
        max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title")
    )
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING, related_name="quizzes"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    # DO NOT EDIT
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=7)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.first_name


class AuthorQuerySet(models.QuerySet):
    def annotate_with_copies_sold(self):
        # Write your solution here
        return self.annotate(copies_sold=Sum("books__copies_sold"))


class AuthorManager(models.Manager.from_queryset(AuthorQuerySet)):
    pass


# AuthorBook.objects.annotate_with_copies_sold().first()
#


class AuthorBook(models.Model):
    # Make sure this manager is available.
    objects = AuthorManager()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}".title()


class BookDjango(models.Model):
    title = models.CharField(max_length=30)
    copies_sold = models.PositiveIntegerField()
    author = models.ForeignKey(
        AuthorBook, on_delete=models.CASCADE, related_name="books"
    )
