# Créez une liste de tuples représentant les commandes d'achat avec les produits et les quantités. Ensuite, créez un
# dictionnaire de prix pour chaque produit. Calculez ensuite le coût total de toutes les commandes et affichez-le.

totalAchat = 0
commandeAchat = [("Pomme", 2), ("Pain", 1), ("Soupe", 7), ("Pâtes", 4), ("Jus d'orange", 2)]

prixProduit = {
    "Pomme" : 10,
    "Pain" : 3,
    "Soupe" : 5,
    "Pâtes" : 4,
    "Jus d'orange" : 6
}

for x in range(len(commandeAchat)) :
    totalAchat = totalAchat + (prixProduit[commandeAchat[x][0]] * commandeAchat[x][1])

print(totalAchat)