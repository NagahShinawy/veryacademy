# Generated by Django 3.2.7 on 2021-10-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lne", "0005_contactus"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactus", options={"verbose_name": "Contact"},
        ),
        migrations.AlterField(
            model_name="contactus", name="phone", field=models.CharField(max_length=13),
        ),
    ]
