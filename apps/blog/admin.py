from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "slug", "author")
    list_editable = ("title", "author")
    prepopulated_fields = {
        "slug": ("title",)
    }  # generated auto slug field based on title
    date_hierarchy = "publish"
    raw_id_fields = (
        "author",
    )  # show FK of one-many relationship instead of drop down list
