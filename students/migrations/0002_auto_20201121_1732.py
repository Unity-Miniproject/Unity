# Generated by Django 3.0.5 on 2020-11-21 17:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bmsit_Students',
            new_name='Students',
        ),
    ]
