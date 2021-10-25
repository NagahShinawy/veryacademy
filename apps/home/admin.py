from django.contrib import admin

from apps.home.models import Note


class ReadOnlyAdminModelMixin(admin.ModelAdmin):
    #  ready only model
    # source: https://stackoverflow.com/questions/54869741/how-to-add-django-admin-read-only-permissions

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AddModelAdminMixin(admin.ModelAdmin):
    #  ready only model
    # source: https://stackoverflow.com/questions/54869741/how-to-add-django-admin-read-only-permissions

    def has_add_permission(self, request):
        return True


class UpdateModelAdminMixin(admin.ModelAdmin):
    #  ready only model
    # source: https://stackoverflow.com/questions/54869741/how-to-add-django-admin-read-only-permissions

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Note)
class NoteModelAdmin(
    AddModelAdminMixin, UpdateModelAdminMixin, ReadOnlyAdminModelMixin
):
    list_display = ("id", "title", "description", "created", "updated", "is_active")
    list_editable = ("title", "description", "is_active")
