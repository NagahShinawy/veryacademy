# Generated by Django 3.2.7 on 2021-09-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20210928_1056"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="dob",
            field=models.DateField(blank=True, null=True),
        ),
    ]
