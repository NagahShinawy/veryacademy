# Generated by Django 3.2.7 on 2021-10-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akhdar', '0002_auto_20211018_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='text'),
        ),
    ]
