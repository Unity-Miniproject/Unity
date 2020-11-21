from django.db import models

# Create your models here.


class videoLink(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    link = models.SlugField()
    discription = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Video Details"