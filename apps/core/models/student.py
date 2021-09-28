from django.db import models
from apps.core.managers import StudentManager, TeacherManager
from apps.core.choices import Gender, ExperienceLevel


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20, choices=ExperienceLevel.choices, default=ExperienceLevel.PRIMARY
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    objects = TeacherManager()

    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, default=Gender.MALE
    )

    objects = StudentManager()

    def __str__(self):
        return self.firstname

    @property
    def is_male(self):
        return self.gender == Gender.MALE

    @property
    def is_female(self):
        return self.gender == Gender.FEMALE
