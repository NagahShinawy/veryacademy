from django.contrib import admin
from apps.core.models import Student, Teacher


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "gender", "age", "teacher")


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "surname")