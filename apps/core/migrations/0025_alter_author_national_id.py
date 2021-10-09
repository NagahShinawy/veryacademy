# Generated by Django 3.2.7 on 2021-10-09 17:31

import apps.core.fields.general
import apps.core.validators.base_validation
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20211009_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='national_id',
            field=apps.core.fields.general.NationalIDField(default='11223344556677', max_length=14, validators=[apps.core.validators.base_validation.NationalIDValidator()]),
        ),
    ]
