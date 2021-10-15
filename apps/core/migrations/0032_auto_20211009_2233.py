# Generated by Django 3.2.7 on 2021-10-09 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0031_medicalitem_medicalitemproxy"),
    ]

    operations = [
        migrations.DeleteModel(name="MedicalItemProxy",),
        migrations.CreateModel(
            name="MedicalItemExport",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("core.medicalitem",),
        ),
    ]
