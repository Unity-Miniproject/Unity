# Generated by Django 3.0.5 on 2020-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('discription', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Video Details',
            },
        ),
    ]
