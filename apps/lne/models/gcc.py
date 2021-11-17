from django.db import models


class RepModelMixin(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Page(RepModelMixin, models.Model):
    title = models.CharField(max_length=100)


class Question(RepModelMixin, models.Model):
    class Level(models.TextChoices):
        EASY = ("easy", "Easy")
        MEDIUM = ("medium", "Medium")
        HARD = ("hard", "Hard")

    title = models.CharField(max_length=256)
    level = models.CharField(choices=Level.choices, max_length=6)
    page = models.ForeignKey(
        to=Page, on_delete=models.PROTECT, related_name="questions"
    )


class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["id"]
