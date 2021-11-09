from django.contrib import admin
from .models import HearingTestData, Member, ContactUs, Page, Question


admin.site.register(HearingTestData)
admin.site.register(Member)


@admin.register(ContactUs)
class ContactModelAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ("id", "name", "phone", "nationalid", "status")
    list_editable = (
        "name",
        "phone",
        "status",
    )


class QuestionModelAdmin(admin.TabularInline):
    model = Question


@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_editable = ("title",)
    inlines = [QuestionModelAdmin]
