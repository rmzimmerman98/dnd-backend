from django.db import models

# Create your models here.
class Initiative(models.Model):
    name = models.CharField(max_length=32)
    initiative = models.IntegerField()
    notes = models.CharField(max_length=100)