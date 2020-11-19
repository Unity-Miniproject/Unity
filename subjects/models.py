from django.db import models


# Create your models here
class WT(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Web Technology and its applications'


class AcA(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Advanced Computer Architectures'


class ML(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Machine Learning'


class SaN(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Storage Area Network'


class CC(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Cloud Computing'


class MlLab(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Machine Learning Laboratory'


class WtLab(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Web Technology Laboratory with mini project'


class project(models.Model):
    section = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Project Work Phase–I + Project work Seminar'
