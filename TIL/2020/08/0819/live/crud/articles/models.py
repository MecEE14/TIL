from django.db import models

# Create your models here.
class House(models.Model):
    parents = models.CharField(max_length=3)
    me = models.TextField()
    brother = models.DateTimeField(auto_now_add=True)
    sister = models.DateTimeField(auto_now=True)