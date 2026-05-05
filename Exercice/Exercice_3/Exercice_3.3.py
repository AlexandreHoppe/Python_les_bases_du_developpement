# Créez un programme qui génère un nombre aléatoire (import random) et permet à l'utilisateur de deviner ce nombre.
# Utilisez des correspondances pour comparer la devinette de l'utilisateur avec le nombre généré et fournir des indices.

import random
import os
import time

nombreAleatoire = random.randint(1, 100)
nombreDeviner = int(input("Devinez le nombre entre 1 et 100 : "))

while nombreDeviner != nombreAleatoire :
    
    if (nombreAleatoire - nombreDeviner) < 0 :
        print("C'est moins")
    elif (nombreAleatoire - nombreDeviner) > 0 :
        print("C'est plus")
        
    
    time.sleep(2)
    os.system('cls')
    nombreDeviner = int(input("Devinez le nombre entre 1 et 100 : "))

print("Correct!")