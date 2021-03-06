from django.contrib import admin

from apps.core.models import (
    ISBN,
    Author,
    BasicProfile,
    Book,
    Category,
    Developer,
    Mobile,
    Quizzes,
    Student,
    Teacher,
    TechLead,
    MedicalItem,
    MedicalItemExport,
    Product,
    Group,
    Account,
    NoteBook,
    TLead,
    Server,
    Ubuntu,
    Centos,
    Person,
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


@admin.register(Person)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "created_date")


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "gender", "created", "updated")
    list_editable = (
        "title",
        "description",
        "gender",
    )


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


@admin.register(Mobile)
class MobileModelAdmin(admin.ModelAdmin):
    list_display = ("id", "brand")


@admin.register(MedicalItem)
class MedicalItemModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "country")


@admin.register(MedicalItemExport)
class MedicalItemExportModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "country")


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created",
    )
    readonly_fields = ("slug",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "price", "is_active")
    readonly_fields = ("slug",)
    list_editable = ("price", "is_active")


@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "gender", "status", "created_at")
    list_editable = ("status",)

    def __init__(self, model, admin_site):
        # reordering model admin fields
        # source : https://stackoverflow.com/questions/2753764/reordering-fields-in-django-model/5231587
        self.fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "gender",
            "status",
        ]
        super().__init__(model, admin_site)


@admin.register(NoteBook)
class NoteBookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "pages")


@admin.register(TLead)
class TLeadModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "dob",
        "team_numbers",
    )

    list_editable = ("team_numbers",)


@admin.register(Ubuntu)
class UbuntuModelAdmin(admin.ModelAdmin):
    list_display = ("id", "hardware", "os", "version")


@admin.register(Centos)
class CentosModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hardware",
        "os",
        "release",
    )
