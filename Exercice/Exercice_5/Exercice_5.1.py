# Commencez par créer une liste de 10 nombres aléatoires compris entre 1 et 100. Ensuite, affichez cette liste générée.
# Après cela, calculez la somme de tous les éléments de la liste et affichez-la.

import random

listeAleatoire = []

for _ in range(0, 10) :
    listeAleatoire.append(random.randint(1, 100))

print(listeAleatoire)
print(sum(listeAleatoire))