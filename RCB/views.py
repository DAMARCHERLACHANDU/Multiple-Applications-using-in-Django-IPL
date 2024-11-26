from django.shortcuts import render

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> RCB Captain is VIRAT KOHLI </h1>')

def vice_captain(request):
    return HttpResponse('<h1> RCB Vice Captain is RAJAT PATIDAR </h1>')

def wicket_keeper(request):
    return HttpResponse('<h1> RCB  Wicket Keeper is SALT </h1>')