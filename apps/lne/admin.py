from django.contrib import admin
from .models import HearingTestData, Member, ContactUs


admin.site.register(HearingTestData)
admin.site.register(Member)


@admin.register(ContactUs)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "nationalid",
    )
    list_editable = (
        "name",
        "phone",
    )
