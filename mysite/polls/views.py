from django.shortcuts import render
from .models import Employe
from .models import Departement
from django.core.paginator import Paginator

maxe=3

def index(request):
    departement=Departement.objects.all 
    return render(request,'departement.html',{"departement":departement})

def index2(request):
    employe=Employe.objects.all()
    paginator = Paginator(employe, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    employes = paginator.get_page(page)


    # page = int(request.GET.get('page',1))
    # page = max(1,page)
    # if int(Employe.objects.count()) < (int(page)-1)*maxe:
    #     page-=1
    # employe=Employe.objects.all()[int(page-1)*(maxe):int(page)*maxe]
    
    # data={}
    # data["employe"] = employe
    # data["page"] = (int(page))
    return render(request,'employe.html',{"employe":employes})