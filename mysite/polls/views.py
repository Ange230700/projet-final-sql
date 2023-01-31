from django.shortcuts import render
from .models import Employe
from .models import Departement
from .models import Postes

from django.core.paginator import Paginator


def indexDepartement(request):
    departement=Departement.objects.all()
    paginator = Paginator(departement, 2) # Show 10 contacts per page

    page2 = request.GET.get('page2')
    departements = paginator.get_page(page2)
    return render(request,'departement.html',{"departement":departements})

def indexEmploye(request):
    employe=Employe.objects.all()
    paginator = Paginator(employe, 2) # Show 10 contacts per page

    page = request.GET.get('page')
    employes = paginator.get_page(page)
    return render(request,'employe.html',{"employe":employes})

def indexPoste(request):
    poste=Postes.objects.all()
    paginator = Paginator(poste, 2) # Show 10 contacts per page

    page = request.GET.get('page')
    postes = paginator.get_page(page)
    return render(request,'poste.html',{"postes":postes})