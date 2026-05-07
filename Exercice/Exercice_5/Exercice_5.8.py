# Créez un dictionnaire de listes représentant différents cours et les étudiants inscrits dans chaque cours. Ajoutez des
# étudiants à chaque cours. Ensuite, demandez à l'utilisateur de saisir le nom d'un cours et affichez la liste des
# étudiants inscrits à ce cours

listeCours = {
    "Développement déclaratif SQL" : ["Steve","John","Bob","Jean","Alex","Henriette"], 
    "Modélisation relationnelle et dénormalisation" : ["Alexia ","Chris","Tyler","Jenna","Tanya","Kane"], 
    "Algorithmique pour le développement sur le langage Python" : ["Terry","Willie","Eddie","Ellis","Violet","Jerry"], 
    "Python : les bases du développement" : ["Ashley","Georgie","Shawn","Kane","Shane","Tony"], 
    "Python OO " : ["Mae","Fraser","Elena","Kyle","Emma","Alba"]

}

print(listeCours[input("Entrez le nom du cours : ")])