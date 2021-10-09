from django.db import models
from apps.core.validators import national_id_validator


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


class InfoModelMixin(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True


class BasicInfoMixin(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Date Of Birth")

    class Meta:
        abstract = True
        ordering = ["id"]

    def __str__(self):
        return self.name


class CreatedModelMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="created datetime")

    class Meta:
        abstract = True


class UpdatedModelMixin(models.Model):
    updated = models.DateTimeField(auto_now=True, verbose_name="last modified datetime")

    class Meta:
        abstract = True


class TimeStampModelMixin(UpdatedModelMixin, CreatedModelMixin):
    """
    Using create & updated fields
    """


class NationalIDField(models.CharField):

    ID_MAX_DIGITS = 14
    ID_EXAMPLE = "11223344556677"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = self.ID_MAX_DIGITS
        kwargs["validators"] = [
            national_id_validator,
        ]
        kwargs["default"] = self.ID_EXAMPLE

        super(NationalIDField, self).__init__(*args, **kwargs)
