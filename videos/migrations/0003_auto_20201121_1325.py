# Generated by Django 3.0.5 on 2020-11-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20201121_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolink',
            name='discription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='videolink',
            name='link',
            field=models.SlugField(),
        ),
    ]