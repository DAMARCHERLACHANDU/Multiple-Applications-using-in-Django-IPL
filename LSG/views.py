from django.shortcuts import render

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> LSG Captain is RISHAB PANT </h1>')

def vice_captain(request):
    return HttpResponse('<h1> LSG Vice Captain is NICHOLAS POORAN </h1>')

def wicket_keeper(request):
    return HttpResponse('<h1> LSG  Wicket Keeper is RISHAB PANT </h1>')