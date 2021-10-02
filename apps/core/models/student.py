from django.db import models
from apps.core.managers import StudentManager, TeacherManager
from apps.core.choices import Gender, ExperienceLevel
from apps.core.fields import ArabicNameField, EnglishNameField, AgeField


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20, choices=ExperienceLevel.choices, default=ExperienceLevel.PRIMARY
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dob = models.DateField(blank=True, null=True)
    objects = TeacherManager()

    def __str__(self):
        return f"{self.firstname}-{self.salary}"


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    name_ar = ArabicNameField(blank=True, null=True, max_length=256)
    name_en = EnglishNameField(blank=True, null=True, max_length=256)
    surname = models.CharField(max_length=100)
    age = AgeField(null=True, blank=True)
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
