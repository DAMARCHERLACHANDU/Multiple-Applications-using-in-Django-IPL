from django.shortcuts import render

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> SRH Captain is PAT CUMMINS </h1>')

def vice_captain(request):
    return HttpResponse('<h1> SRH Vice Captain is NITISH KUMAR REDDY </h1>')

def wicket_keeper(request):
    return HttpResponse('<h1> SRH  Wicket Keeper is KALASEN  </h1>')