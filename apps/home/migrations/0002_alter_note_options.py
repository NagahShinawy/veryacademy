# Generated by Django 3.2.7 on 2021-10-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'default_permissions': ('view', 'add'), 'ordering': ['id']},
        ),
    ]
