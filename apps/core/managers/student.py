from django.db import models
from apps.core.choices import Gender


class StudentManager(models.Manager):

    UNDER_AGE = 18

    def get_by_firstname(self, firstname):
        return self.filter(firstname=firstname)

    def get_by_age(self, age):
        return self.filter(age=age)

    def get_by_age_rage(self, start, end):
        return self.filter(age__range=[start, end])

    def get_under_age(self):
        return self.filter(age__lt=self.UNDER_AGE)

    def get_by_males(self):
        return self.filter(gender=Gender.MALE)

    def get_by_females(self):
        return self.filter(gender=Gender.FEMALE)
