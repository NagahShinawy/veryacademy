from django.contrib import admin
from .models import HearingTestData, Member, ContactUs


admin.site.register(HearingTestData)
admin.site.register(Member)


@admin.register(ContactUs)
class ContactModelAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = (
        "id",
        "name",
        "phone",
        "nationalid",
        "status"
    )
    list_editable = (
        "name",
        "phone",
        "status",
    )
