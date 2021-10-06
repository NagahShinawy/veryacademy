# Generated by Django 3.2.7 on 2021-09-29 14:54

from django.db import migrations

import apps.core.fields.names


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_student_name_ar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="name_ar",
            field=apps.core.fields.names.ArabicNameField(
                blank=True, max_length=256, null=True
            ),
        ),
    ]
