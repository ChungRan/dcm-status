from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View
from crawling.models import *
from django.utils import timezone
import datetime

from crawling import crawling


def minorGallRank(request):
    try:
        # print(request.GET["calendar"])
        date = datetime.datetime.strptime(request.GET["calendar"], '%Y-%m-%d').date()
    except:
        date = timezone.now().date()

    # try:
    crawledDate, crawledDateIsCreated = CrawledDate.objects.get_or_create(date=date)
    ranks = Rank.objects.filter(crawledDate=crawledDate).order_by('rank')
    for rank in ranks:
        if rank.comparedToPreviousDay == 10181018:
            rank.comparedToPreviousDay = 'New'
        elif rank.comparedToPreviousDay > 0:
            rank.comparedToPreviousDay = '+' + str(rank.comparedToPreviousDay)
        elif rank.comparedToPreviousDay == 0:
            rank.comparedToPreviousDay = '-'

    context = {
        'ranks': ranks,
        'date': date
    }

    return render(request, 'ranks/rank.html', context)


def minorGall(request, gall_id):
    gall = get_object_or_404(MinorGall, gallId=gall_id)

    today = timezone.now().date()

    # todayRank
    crawledDate, crawledDateIsCreated = CrawledDate.objects.get_or_create(date=today)
    if gall.rank_set.filter(crawledDate=crawledDate).exists():
        todayRank = str(gall.rank_set.get(crawledDate=crawledDate).rank) + "위"
    else:
        todayRank = '정보없음'

    # averageRank
    availableRankCount = 0
    availableRankTotal = 0
    for i in range(14):
        date = today - datetime.timedelta(i)
        crawledDate, crawledDateIsCreated = CrawledDate.objects.get_or_create(date=date)
        if gall.rank_set.filter(crawledDate=crawledDate).exists():
            availableRankCount += 1
            availableRankTotal += gall.rank_set.get(crawledDate=crawledDate).rank
        else:
            continue
    averageRank = '정보없음' if availableRankCount == 0 else str(availableRankTotal // availableRankCount) + "위"

    # averagePostCount
    averagePostCount = '정보없음'

    context = {
        'gall': gall,
        'todayRank': todayRank,
        'averageRank': averageRank,
        'averagePostCount': averagePostCount,
    }

    return render(request, 'gall/minorGall.html', context)


def crawling_everyday(request):
    crawling.crawlingMinorgaall()
    return HttpResponse("crawling")
