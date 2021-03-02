import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    # SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    title = models.CharField(max_length=100)
    description = models.TextField()
    # sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=true)
    submission_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.submission_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    description = models.TextField()
    article_fk = models.ForeignKey('Article', on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.description
