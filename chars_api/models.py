from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=16)
    level = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    con = models.IntegerField()
    int = models.IntegerField()
    wis = models.IntegerField()
    cha = models.IntegerField()