# Gestion des repas du jour améliorée : Développez un programme interactif qui permet à l'utilisateur de choisir un menu
# pour chaque repas de la journée parmi des options prédéfinies. Utilisez une boucle pour faciliter la saisie des choix
# pour chaque repas et affichez un résumé des choix de repas à la fin. Demandez ensuite à l'utilisateur s'il souhaite
# choisir les repas pour un autre jour. Répétez le processus jusqu'à ce qu'il décide de ne plus choisir de repas

nouvellecommande = True

while nouvellecommande == True :
    petitdejeuner = int(input("\n1. Ceréal \n2. Flocons d'avoine \n3. Tartines Griller \nEntrer le numero du repas voulus pour le petit-déjeuner : "))

    match petitdejeuner :
        case 1 :
            petitdejeunerChoisi = "Ceréals"
            print(petitdejeunerChoisi)
        case 2 :
            petitdejeunerChoisi = "Flocons d'avoine"
            print(petitdejeunerChoisi)
        case 3 :
            petitdejeunerChoisi = "Tartines Griller"
            print(petitdejeunerChoisi)

    déjeuner = int(input("\n1. Burger King \n2. Salade \n3. Tartine \n4. Dagobert \nEntrer le numero du repas voulus pour le déjeuner : "))

    match déjeuner :
        case 1 :
            dejeunerChoisi = "Burger King"
            print(dejeunerChoisi)
            dejeunerChoisi = "le " + dejeunerChoisi
        case 2 :
            dejeunerChoisi = "Salade"
            print(dejeunerChoisi)
            dejeunerChoisi = "la " + dejeunerChoisi
        case 3 :
            dejeunerChoisi = "Tartine"
            print(dejeunerChoisi)
            dejeunerChoisi = "la " + dejeunerChoisi
        case 4 :
            dejeunerChoisi = "Dagobert"
            print(dejeunerChoisi)
            dejeunerChoisi = "le " + dejeunerChoisi

    diner = int(input("\n1. Steak Frite \n2. Pêches au thon \n3. Spaghetti \n4. Blanquette de veau \n5. Vol-au-vent \nEntrer le numero du repas voulus pour le dîner : "))

    match diner :
        case 1 :
            dinerChoisi = "Steak Frite"
            print(dinerChoisi)
            dinerChoisi = "le " + dinerChoisi
        case 2 :
            dinerChoisi = "Pêches au thon"
            print(dinerChoisi)
            dinerChoisi = "les " + dinerChoisi
        case 3 :
            dinerChoisi = "Spaghetti"
            print(dinerChoisi)
            dinerChoisi = "les " + dinerChoisi
        case 4 :
            dinerChoisi = "Blanquette de veau"
            print(dinerChoisi)
            dinerChoisi = "la " + dinerChoisi
        case 5 :
            dinerChoisi = "Vol-au-vent"
            print(dinerChoisi)
            dinerChoisi = "le " + dinerChoisi

    print("\n\nVos choix se sont tournés vers les", petitdejeunerChoisi, "pour le petit-déjeuner,", dejeunerChoisi, "pour le déjeuner, et les", dinerChoisi, "pour le dîner.", sep=(" "))
    if int(input("\n\nVoulez-vous passer une autre commande ? 1. Oui       2.Non : ")) == 2 :
        nouvellecommande = False

print("Bonne journée")