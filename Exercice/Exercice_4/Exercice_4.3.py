# Jeu de devinette de nombre amélioré : Écrivez un jeu interactif où l'ordinateur génère un nombre aléatoire entre 1 et
# 100, et l'utilisateur doit deviner ce nombre. Utilisez une boucle pour permettre à l'utilisateur de faire plusieurs
# tentatives. Après chaque tentative, demandez à l'utilisateur s'il souhaite continuer à jouer. Répétez le processus
# jusqu'à ce qu'il décide de ne plus jouer. Enfin, affichez le nombre de tentatives utilisées pour deviner le nombre.

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