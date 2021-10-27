from django.db import models
from apps.core.validators import national_id_validator
from apps.core.choices import MaritalStatus, Gender
from apps.core.constants import DECIMAL_OPTIONS, NULL_BLANK


class GenderModelMixin(models.Model):
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
        return self.gender == Gender.MALE

    @property
    def is_female(self):
        return self.gender == Gender.FEMALE

    @property
    def is_not_specified(self):
        return self.gender == Gender.NOT_SPECIFIED


class SlugModelMixin(models.Model):
    slug = models.SlugField(max_length=300, blank=True, null=True)

    class Meta:
        abstract = True


class InfoModelMixin(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(null=True, blank=True,  verbose_name="text")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class BasicInfoMixin(GenderModelMixin, models.Model):
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


class IsActiveModelMixin(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Is Available")

    class Meta:
        abstract = True


class MaritalStatusModelMixin(models.Model):
    status = models.CharField(max_length=10, choices=MaritalStatus.choices)

    class Meta:
        abstract = True


class PriceModelMixin(models.Model):
    price = models.DecimalField(**DECIMAL_OPTIONS, **NULL_BLANK)

    class Meta:
        abstract = True


class EmailModelMixin(models.Model):
    email = models.EmailField(verbose_name="Email")

    class Meta:
        abstract = True


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
