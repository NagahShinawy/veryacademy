from django.db import models


class GenderModelMixin(models.Model):
    class Gender(models.TextChoices):
        MALE = ("m", "Male")
        FEMALE = ("f", "Female")
        NOT_SPECIFIED = ("n", "Not Specified")

    gender = models.CharField(
        max_length=1,
        default=Gender.NOT_SPECIFIED,
        choices=Gender.choices,
        verbose_name="Gender",
    )

    class Meta:
        abstract = True

    @property
    def is_male(self):
        return self.gender == self.Gender.MALE

    @property
    def is_female(self):
        return self.gender == self.Gender.FEMALE

    @property
    def is_not_specified(self):
        return self.gender == self.Gender.NOT_SPECIFIED
