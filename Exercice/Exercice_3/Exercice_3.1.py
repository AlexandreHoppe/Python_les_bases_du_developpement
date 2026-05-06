# Créez un programme qui gère les commandes de café en fonction des différentes options telles que la taille, le type de
# café, les extras, etc. Utilisez des correspondances pour traiter chaque option et calculer le prix total de la commande.

tailleCafe = input("Taille : ")
typeCafe = input("Type : ")
extrasCafe = input("Extras : ")

match tailleCafe.lower() :
    case "grand" :
        tailleModificateur = 3

    case "moyen" :
        tailleModificateur = 2

    case "petit" :
        tailleModificateur = 1
    case _ :
        tailleModificateur = 0
        print("Taille non present.")

match typeCafe.lower() :
    case "espresso" :
        typeModificateur = 1
    case "café glacé" :
        typeModificateur = 1.5  
    case "americano" :
        typeModificateur = 1
    case "cappuccino" :
        typeModificateur = 2
    case _ :
        typeModificateur = 0
        print("Type non present.")

match extrasCafe.lower() :
    case "sucre" :
        extrasModificateur = .4
    case "lait" :
        extrasModificateur = .5
    case _ :
        extrasModificateur = 0
        print("Extras non present.")

print("Total : ", tailleModificateur + typeModificateur + extrasModificateur, "€")