from django.db import models


class ExperienceLevel(models.TextChoices):
    PRIMARY = ("primary", "Primary")
    MIDLEVEL = ("midlevel", "Mid Level")
    EXPERT = ("expert", "Expert")
