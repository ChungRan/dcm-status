from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View

from crawling import crawling

def minorGallRank(request):

    return render(request, 'ranks/rank.html')

def crawling_everyday(request):
    crawling.crawlingMinorgaall()
    return HttpResponse("aa")
