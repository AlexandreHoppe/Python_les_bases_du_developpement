# Gestionnaire de commandes de café amélioré :Écrivez un programme interactif qui prend les commandes de café en
# fonction des options telles que la taille, le type de café et les extras. Utilisez une boucle pour permettre à l'utilisateur
# de passer plusieurs commandes et affichez le prix total à la fin de chaque commande. Demandez ensuite à l'utilisateur
# s'il souhaite passer une autre commande et répétez le processus jusqu'à ce qu'il n'en ait plus envie.

nouvellecommande = True

while nouvellecommande == True :
    tailleCafe = int(input("Taille : \n 0.Sortir \n 1.Grand \n 2.Moyen \n 3.Petit \n Entrez la taille voulus : "))

    match tailleCafe :
        case 1 :
            tailleModificateur = 3

        case 2 :
            tailleModificateur = 2

        case 3 :
            tailleModificateur = 1
        case 0 :
            break

    
    typeCafe = int(input("Type : \n 1.Espresso \n 2.Café Glacé \n 3.Americano \n 4.Cappuccino \n Entrez le type voulus : "))
    match typeCafe :
        case 1 :
            typeModificateur = 1
        case 2 :
            typeModificateur = 1.5  
        case 3 :
            typeModificateur = 1
        case 4 :
            typeModificateur = 2
        case 0 :
            break

    extrasCafe = int(input("Extras : \n 1.Sucre \n 2.Lait \n 3.Glaçon \n 4. Pas d'extras :  "))

    match extrasCafe :
        case 1 :
            extrasModificateur = .4
        case 2 :
            extrasModificateur = .5
        case 3 :
            extrasModificateur = 1
        case 0 :
            break

    print("Total : ", tailleModificateur + typeModificateur + extrasModificateur, "€")

print("Bonne journée")