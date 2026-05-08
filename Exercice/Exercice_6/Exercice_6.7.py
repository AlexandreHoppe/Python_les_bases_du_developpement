# Implémentez une fonction inverser_chaine() qui prend une chaîne de caractères en entrée et retourne cette chaîne
# inversée.

def inverser_chaine(listLettre) :
    
    listInverser = []

    for lettre in range(0, len(listLettre), 1) :
        listInverser.append(listLettre[len(listLettre) - (lettre + 1)])
    return listInverser


print(inverser_chaine(['B','o', 'n','j', 'o', 'u', 'r']))