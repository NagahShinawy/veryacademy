# Generated by Django 3.2.7 on 2021-10-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lne", "0007_auto_20211018_1427"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="description",
            field=models.TextField(max_length=300),
        ),
    ]
