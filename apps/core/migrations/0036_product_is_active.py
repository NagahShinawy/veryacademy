# Generated by Django 3.2.7 on 2021-10-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0035_auto_20211014_1322"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Is Available"),
        ),
    ]
