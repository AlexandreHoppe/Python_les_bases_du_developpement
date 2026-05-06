# Créez un programme qui génère un nombre aléatoire (import random) et permet à l'utilisateur de deviner ce nombre.
# Utilisez des correspondances pour comparer la devinette de l'utilisateur avec le nombre généré et fournir des indices.

import random


nombreAleatoire = random.randint(1, 100)
nombreDeviner = int(input("Devinez le nombre entre 1 et 100 : "))

    
if (nombreAleatoire - nombreDeviner) < 0 :
    print("C'est moins")
elif (nombreAleatoire - nombreDeviner) > 0 :
    print("C'est plus")
elif (nombreAleatoire == nombreDeviner ) :
    print("Correct!")