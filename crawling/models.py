from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


class CrawledDate(models.Model):
    date = models.DateField(default=timezone.now, unique=True)

    def __str__(self):
        return str(self.date)


class Rank(models.Model):
    def comparedToPreviousDay_default(self):
        try:
            yesterday = self.crawledDate.date - datetime.timedelta(1)
            # yesterdayCrawledDate, yesterdayCrawledDateIsCreated = CrawledDate.get_or_create(date = yesterday)
            yesterdayCrawledDate = CrawledDate.objects.get(date=yesterday)
            yesterdayRank = Rank.objects.get(crawledDate=yesterdayCrawledDate, gall=self.gall).rank
            return yesterdayRank - self.rank
        except:
            return 10181018

    crawledDate = models.ForeignKey("CrawledDate", on_delete=models.CASCADE, null=True)
    rank = models.PositiveIntegerField()
    gall = models.ForeignKey('Gall', on_delete=models.CASCADE)
    comparedToPreviousDay = models.IntegerField(null=True)

    def __str__(self):
        return str(self.crawledDate.date) + " " + self.gall.name + " 갤러리 순위"


@receiver(post_save, sender=Rank)
def create_comparedToPreviosday(sender, instance, created, **kwargs):
    if created:
        instance.comparedToPreviousDay = instance.comparedToPreviousDay_default()
        instance.save()


class Gall(models.Model):
    name = models.TextField()
    gallId = models.TextField(unique=True)
    content = models.TextField(blank=True)
    openingDate = models.DateField(null=True)

    def __str__(self):
        return self.name + " 갤러리"


class MinorGall(Gall):
    pass


class MiniGall(Gall):
    pass

# class MajorGall(Gall):
#     pass


class StatPostCount(models.Model):
    date = models.DateField(default=timezone.now)
    gall = models.ForeignKey('Gall', on_delete=models.CASCADE)
    postCount = models.PositiveIntegerField()
