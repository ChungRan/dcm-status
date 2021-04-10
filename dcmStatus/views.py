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

    # except:
    #     galls = [{
    #         'rank': '#',
    #         'name': '해당 일자의 데이터를 찾을 수 없습니다',
    #         'gall_id': 'DATA_NULL'
    #     }]

    context = {
        'ranks': ranks,
        'date': date
    }

    return render(request, 'ranks/rank.html', context)


def minorGall(request, gall_id):
    return HttpResponse("기능 개발중입니다")


def crawling_everyday(request):
    crawling.crawlingMinorgaall()
    return HttpResponse("aa")
