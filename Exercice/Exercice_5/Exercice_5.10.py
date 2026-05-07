# Créez une liste de dictionnaires représentant les informations des employés avec leur nom, salaire et département.
# Calculez la somme des salaires pour chaque département, puis calculez la moyenne des salaires pour chaque
# département. Enfin, affichez les moyennes des salaires pour chaque département.

listeEmployer = {
    "employeUn" : {
        "Nom" : "Jerry",
        "Salaire" : 2500,
        "Département" : "IT"
    },
    "employeDeux" : {
        "Nom" : "Ashley",
        "Salaire" : 1000,
        "Département" : "Exécutive"
    },
    "employeTrois" : {
        "Nom" : "Georgie",
        "Salaire" : 3000,
        "Département" : "IT"
    },
    "employeQuatre" : {
        "Nom" : "Shawn",
        "Salaire" : 1000,
        "Département" : "Ventes"
    },
    "employeCinq" : {
        "Nom" : "Kane",
        "Salaire" : 2500,
        "Département" : "Finance"
    },
    "employeSix" : {
        "Nom" : "Shane",
        "Salaire" : 1000,
        "Département" : "IT"
    },
    "employeSept" : {
        "Nom" : "Tony",
        "Salaire" : 2000,
        "Département" : "Ventes"
    },
    "employeHuit" : {
        "Nom" : "Mae",
        "Salaire" : 2500,
        "Département" : "Ventes"
    },
    "employeNeuf" : {
        "Nom" : "Fraser",
        "Salaire" : 2000,
        "Département" : "IT"
    },
    "employeDix" : {
        "Nom" : "Elena",
        "Salaire" : 2500,
        "Département" : "Exécutive"
    }
}

sommeSalaire = [0, 0, 0, 0]
moyenneSalaire = [0, 0, 0, 0]


for x, obj in listeEmployer.items() :
    print(obj["Département"])
    
    if obj["Département"] == "Exécutive" :
        sommeSalaire[0] = sommeSalaire[0] + listeEmployer[x]["Salaire"]

    elif obj["Département"] == "IT" :
        sommeSalaire[1] = sommeSalaire[1] + listeEmployer[x]["Salaire"]

    elif obj["Département"] == "Ventes" :
        sommeSalaire[2] = sommeSalaire[2] + listeEmployer[x]["Salaire"]

    elif obj["Département"] == "Finance" :
        sommeSalaire[3] = sommeSalaire[3] + listeEmployer[x]["Salaire"]



print(sommeSalaire)
    #test = listeEmployer[x]["Salaire"]
    #print(test)