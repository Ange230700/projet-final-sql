from django.contrib import admin
from .models import Employe,Departement,Postes
# Register your models here.

# class DepartementAdmin(admin.ModelAdmin):
#     list_display = ("id","nom","nombre_personne_departement","date_de_creation_du_departement","budget_annuel_du_departement","responsable_departement")
    
admin.site.register(Employe)
admin.site.register(Departement)
admin.site.register(Postes)
