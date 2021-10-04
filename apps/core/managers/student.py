from itertools import chain
from django.db import models
from apps.core.choices import Gender


class StudentManager(models.Manager):

    UNDER_AGE = 18
    PRIMARY_CLASSES = range(1, 4)  # 1 : 3
    SECONDARY_CLASSES = range(4, 7)  # 4 : 6

    def get_by_firstname(self, firstname):
        return self.filter(firstname__icontains=firstname)

    def get_by_age(self, age):
        return self.filter(age=age)

    def get_by_age_rage(self, start, end):
        return self.filter(age__range=[start, end])

    def get_under_age(self):
        return self.filter(age__lt=self.UNDER_AGE)

    def get_males(self):
        return self.filter(gender=Gender.MALE)

    def get_females(self):
        return self.filter(gender=Gender.FEMALE)

    def get_under_age_females(self):
        return self.get_females() & self.get_under_age()

    def get_under_age_males(self):
        return self.get_males() & self.get_under_age()

    def primary_class(self):
        return self.filter(classroom__in=self.PRIMARY_CLASSES)

    def secondary_class(self):
        return self.filter(classroom__in=self.SECONDARY_CLASSES)
