# Generated by Django 3.0.5 on 2021-01-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201230_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
