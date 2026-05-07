# Générez deux ensembles de nombres aléatoires compris entre 1 et 20. Affichez ces deux ensembles générés. Enfin,
# trouvez l'intersection des deux ensembles et affichez-la.

import random

listeAleatoire = set()
listeAleatoireDeux = set()

for _ in range(0, 10, 1) :
    listeAleatoire.add(random.randint(1, 20))
    listeAleatoireDeux.add(random.randint(1, 20))
    

print(listeAleatoire, listeAleatoireDeux, sep="          ", end='\n\n\n')
print(listeAleatoire.intersection(listeAleatoireDeux))