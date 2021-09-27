from django.db import models
from apps.core.managers import StudentManager
from apps.core.choices import Gender


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, default=Gender.male
    )

    objects = StudentManager()

    def __str__(self):
        return self.firstname

    @property
    def is_male(self):
        return self.gender == self.Gender.male

    @property
    def is_female(self):
        return self.gender == self.Gender.female
