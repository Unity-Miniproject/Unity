# Generated by Django 3.0.5 on 2020-12-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterField(
            model_name='users',
            name='teacher',
            field=models.BooleanField(default=True),
        ),
    ]
