from django.contrib import admin

from apps.home.models import Note


@admin.register(Note)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created", "updated", "is_active")
    list_editable = ("title", "description", "is_active")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
