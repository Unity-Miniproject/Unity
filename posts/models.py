from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length=50)
    question = RichTextField()
    answer1 = RichTextField()
    # answer2 = RichTextField(blank=True, null=True)
    # answer3 = RichTextField(blank=True, null=True)
    # answer4 = RichTextField(blank=True, null=True)
    # answer5 = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('detailed', kwargs={'pk': self.pk})
