# Generated by Django 3.2.7 on 2021-10-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="more",),
    ]
