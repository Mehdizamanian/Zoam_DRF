from django.db import models


class Article (models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(max_length=50)
    author = models.CharField(max_length=100)
    status= models.BooleanField(default=False)

# Create your models here.
