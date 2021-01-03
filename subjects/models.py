from django.db import models

# Create your models here.


class Modelnames(models.Model):
    modelname = models.CharField(max_length=100)

    def __str__(self):
        return modelname


class Section(models.Model):
    name = models.CharField(max_length=1, primary_key=True)
    fullname = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Section'

class Branch(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    fullname = models.CharField(max_length=50) 

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Branch'
class Semester(models.Model):
    name = models.CharField(max_length=1, primary_key=True)
    fullname = models.CharField(max_length=20) 

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Semester'


class newClasses(models.Model):
    classId = models.CharField(max_length=10, primary_key=True)
    className = models.CharField(max_length=50)
    classSection = models.CharField(max_length=50)
    classBranch = models.CharField(max_length=50)
    classSemester = models.CharField(max_length=10)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    createdDate = models.DateTimeField()

    def __str__(self):
        return self.classId

    class Meta:
        verbose_name_plural = 'Classes'
