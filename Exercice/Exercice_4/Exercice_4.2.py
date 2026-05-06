# Créez un programme qui demande à l'utilisateur d'entrer son âge. Utilisez un opérateur ternaire pour vérifier si
# l'utilisateur est majeur ou mineur. Affichez ensuite un message approprié en fonction de la réponse.

ageUtilisateur = int(input("Entrez votre age : "))

if ageUtilisateur < 18 : print("Vous etes mineur.") 
else : print("Vous etes majeur.")