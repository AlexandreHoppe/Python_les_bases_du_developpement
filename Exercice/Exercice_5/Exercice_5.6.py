# Générez une liste de 10 nombres aléatoires compris entre 1 et 50. Affichez cette liste générée. Ensuite, filtrez les
# nombres pairs de la liste et créez une nouvelle liste ne contenant que ces nombres pairs. Enfin, affichez la nouvelle
# liste contenant uniquement les nombres pairs.

import random

listeAleatoire = []
listeAleatoirePaire = []

for _ in range(0, 10) :
    listeAleatoire.append(random.randint(1, 50))

print(listeAleatoire)

for x in range(9) : 
    print(x)
    if listeAleatoire[x] % 2 == 0 :
        #print(x)
        listeAleatoirePaire.append(listeAleatoire[x])

for y in listeAleatoirePaire :
    listeAleatoire.remove(y)

print(listeAleatoirePaire)