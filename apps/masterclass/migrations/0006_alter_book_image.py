# Generated by Django 3.2.7 on 2021-11-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("masterclass", "0005_auto_20211107_0947"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                default="",
                height_field="height",
                upload_to="photos/",
                width_field="width",
            ),
        ),
    ]
