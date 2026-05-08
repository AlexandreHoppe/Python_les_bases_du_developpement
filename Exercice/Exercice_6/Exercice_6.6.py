# Créez une fonction nombres_pairs_impairs() qui prend une liste de nombres en entrée et retourne deux listes
# distinctes, l'une contenant les nombres pairs et l'autre les nombres impairs.

def nombres_pairs_impairs(listeNombre) :

    listepairs = []
    listeimpairs = []

    for x in listeNombre : 
        if x % 2 == 0 :
            listepairs.append(x)
        elif x % 2 != 0 :
            listeimpairs.append(x)
    
    return listepairs, listeimpairs

listeNombre = [15, 20, 17, 10, 12, 18, 18]
print(nombres_pairs_impairs(listeNombre))  

