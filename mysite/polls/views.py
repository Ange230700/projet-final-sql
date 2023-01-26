from django.shortcuts import render
from .models import Departement

def index(request):
    departement=Departement.objects.all 
    return render(request,'departement.html',{"departement":departement})