from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Students(models.Model):
    SEMESTER = (
        ('1', 'First Semester'),
        ('2', 'Second Semester'),
        ('3', 'Third Semester'),
        ('4', 'Fourth Semester'),
        ('5', 'Fifth Semester'),
        ('6', 'Sixth Semester'),
        ('7', 'Seventh Semester'),
        ('8', 'Eighth Semester'),
    )
    BRANCHES = (
        ('CSE', 'Computer Science Engineering'),
        ('ISE', 'Information Science Engineering'),
        ('ECE', 'Electronic Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CVE', 'Civil Engineering'),
        ('AI & ML', 'Artificial Intelligence and Machine Learning.'),
        ('TCE', 'Telecommunications Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    usn = models.CharField(max_length=10, primary_key=True, blank=True)
    name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=254, )
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=True)
    branch = models.CharField(max_length=10, choices=BRANCHES, blank=True)
    profile = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Students Details'
