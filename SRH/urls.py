from django.urls import path

from SRH.views import *

urlpatterns = [
     path('captain/',captain,name='captian'),
    path('vice_captain/',vice_captain,name='vice_captain'),
    path('wicket_keeper/',wicket_keeper,name='wicket_keeper')
]
