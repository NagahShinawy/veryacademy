# Generated by Django 3.2.7 on 2021-11-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lne', '0013_populate_cities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['id'], 'verbose_name_plural': 'Cities'},
        ),
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]