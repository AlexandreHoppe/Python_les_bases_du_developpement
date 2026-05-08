# Écrivez une fonction compte_mots() qui prend une chaîne de caractères représentant une phrase en entrée et retourne
# le nombre de mots dans cette phrase.

def compte_mots(chaineCaracteres) :
    nombreDeMot = 0

    for caracteres in chaineCaracteres :
        if caracteres == ' ' or caracteres == '.':
            nombreDeMot += 1

    return nombreDeMot

chaineCaracteres = "Comment ce passe votre journee."

print("La phrase contien", compte_mots(chaineCaracteres), "mots.", sep=' ')