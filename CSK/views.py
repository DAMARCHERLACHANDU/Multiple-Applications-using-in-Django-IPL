from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> CSK Captain is RUTURAJ GAIKWAD </h1>')

def vice_captain(request):
    return HttpResponse('<h1> CSK Vice Captain is RAVINDRA JADEJA </h1>')

def wicket_keeper(request):
    return HttpResponse('<h1> CSK Wicket Keeper is MS DHONI </h1>')


