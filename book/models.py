from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()