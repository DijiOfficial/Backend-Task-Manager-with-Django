from pyexpat import model
from django.db import models

# Create your models here.
class tasks(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateField()
    done = models.BooleanField()