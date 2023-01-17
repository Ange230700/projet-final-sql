<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../styles/styles_insert.css"/>

    <title>Document</title>
</head>
<body>
    <div class="header">
        <div class="titleHeader">
            <h1>SQL</h1>
        </div>
    </div>    
    <div class="formulaire">
        <form action="/home" method="POST">
        <p>Nom</p>
        <input type="text" name="nom">
        <p>Prénom</p>
        <input type="text" name="Prenom">
        <p>Age</p>
        <input type="text" name="age">
        <p>Date de naissance</p>
        <input type="text"name="birthday">
        <p>Genre</p>
        <select name="Genre" id="Genre-select">
            <option value="femme">Femme</option>
            <option value="homme">Homme</option>
        </select>
        <p>Téléphone</p>
        <input type="text" name="telephone">
        <p>Adresse</p>
        <input type="text" name="adresse">
        <p>Email</p>
        <input type="text" name="email">
        <p>Nombre d'enfant</p>
        <input type="text" name="nombreEnfant">
        <p>Marié</p>
        <select name="marie" id="Genre-select">
            <option value="false">Non</option>
            <option value="true">Oui</option>
        </select>
        <p>Type contrat</p>
        <select name="contrat" id="contrat-select">
            <option value="CDD">CDD</option>
            <option value="CDI">CDI</option>
            <option value="Temps partiel">Temps partiel</option>
            <option value="Saisonnier">Saisonnier</option>
            <option value="Contrat de travail temporaire">Contrat de travail temporaire</option>
        </select>
        <p>Salaire</p>
        <input type="text" name="salaire">
        <p>Numéro d'employé</p>
        <input type="text" name="numero_Employee">
        <p>Date d'embauche</p>
        <input type="text" name="date_embauche">
        <p>Poste</p>
        <input type="text" name="poste">
        <p>Département</p>
        <input type="text" name="departement">
        <p>Responsable hiérarchique</p>
        <input type="text" name="reponsable_hiérarchique">
        <div class="submit">
            <input type="submit" >
        </div>
        </form>
    </div>
    <div class="footer"></div>
</body>
</html>