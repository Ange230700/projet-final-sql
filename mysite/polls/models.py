from django.db import models

class Employe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,default='NONE')
    prenom = models.CharField(max_length=100,default='NONE')
    poste = models.CharField(max_length=100,default='NONE')
    age = models.IntegerField()
    genre = models.CharField(max_length=100,default='NONE',choices=[("OPTION_1", "Homme"),("OPTION_2",  "Femme"),("OPTION_3", "Autre")])
    salaire = models.IntegerField()
    type_contract = models.CharField(max_length=100,default='CDD',choices=[("OPTION_1", "CDD"),("OPTION_2",  "CDI"),("OPTION_3", "Autre")])
    adresse_email = models.CharField(max_length=100,default='NONE')
    date_embauche = models.DateField()
    numero_tel = models.CharField(max_length=100,default='NONE')
    adresse = models.CharField(max_length=100,default='NONE')
    date_de_naissance = models.DateField()
    numero_d_employe = models.CharField(max_length=100,default='NONE')
    nombre_d_enfants = models.IntegerField(default=0)
    conges_payes_restants = models.IntegerField()

class Departement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,default='NONE')
    nombre_personne_departement = models.IntegerField()
    date_de_creation_du_departement = models.DateField()
    budget_annuel_du_departement = models.IntegerField()
    responsable_departement = models.ForeignKey(Employe, on_delete=models.CASCADE)

class Postes(models.Model):
    id = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100,default='NONE')
    Niveau_hiérarchique = models.CharField(max_length=100,default='NONE')
    Salaire = models.IntegerField()
    Département_id = models.ForeignKey(Departement, on_delete=models.CASCADE)
    Statutposte = models.BooleanField()
    type_contrat = models.IntegerField()
