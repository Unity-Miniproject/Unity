# Generated by Django 3.0.5 on 2020-11-22 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('usn', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('semester', models.CharField(blank=True, choices=[('1', 'First Semester'), ('2', 'Second Semester'), ('3', 'Third Semester'), ('4', 'Fourth Semester'), ('5', 'Fifth Semester'), ('6', 'Sixth Semester'), ('7', 'Seventh Semester'), ('8', 'Eighth Semester')], max_length=1)),
                ('branch', models.CharField(blank=True, choices=[('CSE', 'Computer Science Engineering'), ('ISE', 'Information Science Engineering'), ('ECE', 'Electronic Engineering'), ('ME', 'Mechanical Engineering'), ('CVE', 'Civil Engineering'), ('AI & ML', 'Artificial Intelligence and Machine Learning.'), ('TCE', 'Telecommunications Engineering'), ('EEE', 'Electrical and Electronics Engineering')], max_length=10)),
                ('profile', models.ImageField(blank=True, upload_to='uploads')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students Details',
            },
        ),
    ]
