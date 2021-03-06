# Generated by Django 3.2.7 on 2021-11-17 08:33

from django.db import migrations

CITIES = [
    {"name": "Cairo"},
    {"name": "Riyad"},
    {"name": "Makka"},
    {"name": "Dammam"},
    {"name": "Gadda"},
]


def forward(apps, schema_editor):
    City = apps.get_model("lne", "City")

    cities = [City(**city) for city in CITIES]
    City.objects.bulk_create(cities)


class Migration(migrations.Migration):

    dependencies = [
        ("lne", "0012_city"),
    ]

    operations = [
        migrations.RunPython(forward),
    ]
