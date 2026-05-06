# Écrivez un programme qui demande à l'utilisateur d'entrer un mot. Utilisez une boucle pour inverser l'ordre des lettres
# du mot et affichez le mot inversé à la fin.

listLettre = []
motEntre = str(input("Entrez un mot : "))

for x in motEntre :
    listLettre.append(x)

for y in range(0, len(listLettre), 1) :
    print(listLettre[len(listLettre) - (y + 1)])