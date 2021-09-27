from django.db import models
from apps.core.choices import Gender


class StudentManager(models.Manager):

    def get_by_firstname(self, firstname):
        return self.filter(firstname=firstname)

    def get_by_age(self, age):
        return self.filter(age=age)

    def get_by_age_rage(self, start, end):
        return self.filter(age__range=[start, end])

    def get_by_males(self):
        return self.filter(gender=Gender.male)

    def get_by_females(self):
        return self.filter(gender=Gender.female)
