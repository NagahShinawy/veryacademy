# Generated by Django 3.2.7 on 2021-10-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_auto_20211002_0921"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="salary",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
