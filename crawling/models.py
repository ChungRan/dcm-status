from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class CrawledDate(models.Model):
    date = models.DateField(default=timezone.now, unique=True)


class Rank(models.Model):
    def comparedToPreviousday_default(self):
        try:
            yesterday = self.date.date - datetime.timedelta(1)
            yesterdayRank = Rank.objects.get(date=CrawledDate.objects.get(
                date=yesterday), gall_id=self.gall_id).rank
            return yesterdayRank - self.rank
        except:
            return 10181018

    date = models.ForeignKey("CrawledDate", on_delete=models.CASCADE, null=True)
    rank = models.IntegerField()
    name = models.TextField()
    gall_id = models.TextField()
    comparedToPreviousday = models.IntegerField(null=True)


@receiver(post_save, sender=Rank)
def create_comparedToPreviosday(sender, instance, created, **kwargs):
    if created:
        instance.comparedToPreviousday = instance.comparedToPreviousday_default()
        instance.save()
