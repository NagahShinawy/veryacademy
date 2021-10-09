from django.contrib import admin

from apps.core.models import (
    Author,
    BasicProfile,
    Book,
    Category,
    Quizzes,
    Student,
    Teacher,
    Developer,
    TechLead,
    ISBN,
)


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
    list_display = ("id", "firstname", "surname", "level", "salary", "dob", "gender")
    list_editable = ("dob", "salary", "gender")


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "has_offer", "author", "status", "slug")
    list_editable = ("has_offer", "status")


@admin.register(ISBN)
class ISBNModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")


@admin.register(Quizzes)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created")
    list_editable = ("title", "category")


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "gender", "created", "updated")
    list_editable = list_display[1:-2]


@admin.register(BasicProfile)
class BasicProfileModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "dob")
    list_editable = ("email",)


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(TechLead)
class TechLeadModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "senior_exp")
