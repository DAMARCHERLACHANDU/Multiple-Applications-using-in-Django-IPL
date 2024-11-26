from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> MI Captain is HARDIK PANDIYA </h1>')

def vice_captain(request):
    return HttpResponse('<h1> MI Vice Captain is SKY </h1>')

def wicket_keeper(request):
    return HttpResponse('<h1> MI Wicket Keeper is ISHAN KISHAN </h1>')