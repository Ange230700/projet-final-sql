from django.db import models

class Employe(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste_id = models.IntegerField()
    age = models.IntegerField()
    departement_id = models.IntegerField()
    genre = models.CharField(max_length=100)
    salaire = models.IntegerField()
    type_contract = models.IntegerField()
    adresse_email = models.CharField(max_length=100)
    date_embauche = models.DateField()
    numero_tel = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    numero_d_employe = models.CharField(max_length=100)
    nombre_d_enfants = models.IntegerField()
    conges_payes_restants = models.IntegerField()
    responsable_hierarchique = models.IntegerField()

class Postes(models.Model):
    id = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Niveau_hiérarchique = models.CharField(max_length=100)
    Salaire = models.IntegerField()
    Département_id = models.IntegerField()
    Statutposte = models.BooleanField()
    type_contrat = models.IntegerField()


class Departement(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    nombre_personne_departement = models.IntegerField()
    date_de_creation_du_departement = models.DateField()
    budget_annuel_du_departement = models.IntegerField()
    responsable_departement = models.IntegerField()