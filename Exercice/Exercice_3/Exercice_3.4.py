# Créez un programme qui calcule l'indice de masse corporelle (IMC) d'une personne en fonction de son poids et de sa
# taille. Utilisez des correspondances pour interpréter et catégoriser l'IMC résultant en différentes catégories de poids.

taille = int(input("Taille (en cm): ")) / 100
poids = int(input("Poids (en kg): "))

indiceMasseCorporelle = poids / (taille*taille)

if indiceMasseCorporelle > 30 :
    poidsCategorie = "Obésité"
elif indiceMasseCorporelle > 25 :
    poidsCategorie = "Surpoids"
elif indiceMasseCorporelle > 18.5 :
    poidsCategorie = "Poids idéal"
elif indiceMasseCorporelle < 18.5 :
    poidsCategorie = "Maigreur"

print("Votre IMC est de", indiceMasseCorporelle, "et vous etes dans la categorie", poidsCategorie, sep=(" "))