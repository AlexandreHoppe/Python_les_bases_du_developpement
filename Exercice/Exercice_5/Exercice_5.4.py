# Créez un dictionnaire contenant les prix de quelques fruits tels que la pomme, la banane et l'orange. Demandez à
# l'utilisateur de saisir le nom d'un fruit, puis affichez le prix correspondant à ce fruit s'il existe dans le dictionnaire.

prixFruit = {

    "pomme" : 1,
    "poire" : 1.5,
    "orange" : 2,
    "kiwi" : 3,
    "pêches" : .5

}

choixUtilisateur = input("Entrez le nom d'un fruit : ")

print(prixFruit[choixUtilisateur.lower()])