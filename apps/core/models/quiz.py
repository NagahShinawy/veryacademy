from django.db import models
from django.utils.translation import gettext_lazy as _


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
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING, related_name="quizzes")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
