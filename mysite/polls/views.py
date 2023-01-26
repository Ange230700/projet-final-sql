from django.shortcuts import render
# from .models import Projet

def index(request):
    
    return render(request,'insert.html')