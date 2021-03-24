from django.db import models

# Create your models here.

class Rank(models.Model):
    date = models.DateField(default = timezone.now())
    rank = models.IntegerField()
    name = models.TextField()
    url = models.URLField()

