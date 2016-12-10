from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1000, default = '')


