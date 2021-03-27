from django.shortcuts import render, get_object_or_404
from django.views.generic import View

def minorGallRank(request):

    return render(request, 'ranks/rank.html')
