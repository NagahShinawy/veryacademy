from django.contrib import admin
from apps.core.models import Student, Teacher


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "gender", "dob", "teacher", "classroom")
    list_editable = ("dob", )


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "surname", "level", "salary", "dob")
    list_editable = ("dob",)
