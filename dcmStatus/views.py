from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import Http404, HttpResponse

from . import crawling

def test(request):
    a = crawling.crawlingTest()
    return HttpResponse(a)