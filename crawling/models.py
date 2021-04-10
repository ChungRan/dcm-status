from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


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


class Gall(models.Model):
    name = models.TextField()
    gallId = models.TextField(unique=True)
    content = models.TextField(blank=True)
    openingDate = models.DateField(null=True)


class MinorGall(Gall):
    pass


class MiniGall(Gall):
    pass

# class MiniGall(Gall):
#     pass

# 최근 2주간 평균순위
# 최근 2주간 평균 게시글 수


class StatPostCount(models.Model):
    date = models.DateField(default=timezone.now)
    gall = models.ForeignKey('Gall', on_delete=models.CASCADE)
    postCount = models.PositiveIntegerField()
