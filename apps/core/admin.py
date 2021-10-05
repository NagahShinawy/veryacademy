from django.contrib import admin
from apps.core.models import Student, Teacher, Book


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstname",
        "gender",
        "age",
        "teacher",
        "classroom",
        "salary",
    )
    list_editable = ("age", "salary")
    list_filter = ("classroom",)


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "surname", "level", "salary", "dob")
    list_editable = ("dob", "salary")


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "has_offer")
    list_editable = ("has_offer", )
