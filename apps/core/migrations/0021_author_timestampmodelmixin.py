# Generated by Django 3.2.7 on 2021-10-09 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20211009_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampModelMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created datetime')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='last modified datetime')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('timestampmodelmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampmodelmixin')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'Not Specified')], default='n', max_length=1, verbose_name='Gender')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.timestampmodelmixin', models.Model),
        ),
    ]