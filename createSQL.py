import sqlite3
conn = sqlite3.connect("SQLEmploye.db")
cur = conn.cursor()

sql = "CREATE TABLE Employe(id INTEGER PRYMARY KEY NOT NULL,Nom VARCHAR(100),Prenom VARCHAR(100),poste_id INTEGER,age INTEGER,departement_id INTEGER,genre VARCHAR(100),salaire INTEGER,type_contract INTEGER, adresse_email VARCHAR(100),date_embauche DATE,numero_tel VARCHAR(100),adresse VARCHAR(100),Date_de_naissance DATE,Numéro_d_employe VARCHAR(100),Nombre_d_enfants INTEGER,Congés_payés_restants INTEGER,Responsable_hiérarchique INTEGER)"
cur.execute(sql)
conn.commit()
sql = "CREATE TABLE postes(id INTEGER PRYMARY KEY NOT NULL,Nom VARCHAR(100),Niveau_hiérarchique VARCHAR(100),Salaire INTEGER,Département_id INTEGER,Statutposte BOOL,type_contrat INTEGER)"
cur.execute(sql)
conn.commit()
sql = "CREATE TABLE departement(id INTEGER PRYMARY KEY NOT NULL,Nom VARCHAR(100),Nombre_personne_département INTEGER,Date_de_creation_du_département DATE,Budget_annuel_du_département INTEGER,responsable_département INTEGER)"
cur.execute(sql)
conn.commit()