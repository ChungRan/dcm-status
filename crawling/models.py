from django.db import models
from django.utils import timezone

# Create your models here.
class CrawledDate(models.Model):
    date = models.DateField(default = timezone.now, unique = True)





class Rank(models.Model):
    date = models.ForeignKey("CrawledDate", on_delete = models.CASCADE, null = True)
    rank = models.IntegerField()
    name = models.TextField()
    gall_id = models.TextField()

