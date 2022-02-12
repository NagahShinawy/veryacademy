from django.contrib import admin
from .models import Company, Director


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "legal_name", "incorporation_date")


@admin.register(Director)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "start_date", "end_date")
