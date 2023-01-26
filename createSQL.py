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

# for i in range(50) :
#     sqlRequest = "INSERT INTO gares (id, idReseau, gare_Voyageur, Fret,TotalVoyageur2017,TotalVoyageur2018,TotalVoyageur2019,TotalVoyageur2020,TotalVoyageur2021,departement,commune,CoordonateX,CoordonateY) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     total2017=0
#     total2018=0
#     total2019=0
#     total2020=0
#     total2021=0
#     commune = data[i]["fields"]["commune"]
#     getIt = False
#     for j in range(2970) :
#         if Visiteur[j]["fields"]["nom_gare"].upper() == commune :
#             total2017=int(Visiteur[j]["fields"]["totalvoyageurs2017"])
#             total2018=int(Visiteur[j]["fields"]["total_voyageurs_2018"])
#             total2019=int(Visiteur[j]["fields"]["total_voyageurs_non_voyageurs_2019"])
#             total2020=int(Visiteur[j]["fields"]["total_voyageurs_2020"])
#             total2021=int(Visiteur[j]["fields"]["total_voyageurs_non_voyageurs_2021"])
#             break
#     value = (i,data[i]["fields"]["idreseau"],data[i]["fields"]["voyageurs"],data[i]["fields"]["fret"],total2017,total2018,total2019,total2020,total2021, data[i]["fields"]["departemen"],commune,data[i]["fields"]["geo_shape"]["coordinates"][0],data[i]["fields"]["geo_shape"]["coordinates"][1])
#     cur.execute(sqlRequest, value)
#     conn.commit()
# cur.close()
# conn.close()