# Generated by Django 3.2.7 on 2021-10-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_post_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="", unique_for_date="publish"),
        ),
    ]