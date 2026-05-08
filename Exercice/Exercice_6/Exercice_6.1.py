# Écrivez une fonction nommée calcul_moyenne() qui prend une liste de notes en entrée et retourne la moyenne de ces notes.

def calcul_moyenne(listeNote) :
    return sum(listeNote) / len(listeNote)

listeNote = [15, 20, 17, 10, 12, 18, 18]

print (calcul_moyenne(listeNote))