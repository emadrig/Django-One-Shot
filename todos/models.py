from django.db import models

# Create your models here.
class Todos(models.Model):
    information = models.CharField(max_length=200)
