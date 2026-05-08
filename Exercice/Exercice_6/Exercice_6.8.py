# Créez une fonction valider_mot_de_passe() qui prend un mot de passe en entrée et vérifie s'il répond à certains
# critères de complexité (longueur minimale, présence de chiffres, de lettres majuscules et minuscules, de caractères
# spéciaux, etc.). La fonction devrait renvoyer True si le mot de passe est valide et False sinon.

def valider_mot_de_passe(motDePasse) :
    chiffresPresent = False
    lettresMajuscules = False
    lettresMinuscules = False
    lettresSpecial = True

    if len(motDePasse) < 6 :
        return False
    else :
        for  caractere in motDePasse :
            if caractere.isnumeric():
                chiffresPresent = True
            elif caractere.isupper() :
                lettresMajuscules = True
            elif caractere.islower() :
                lettresMinuscules = True
            elif not(caractere.isalpha()) :
                lettresSpecial = True
            
        if chiffresPresent and lettresMajuscules and lettresMinuscules and lettresSpecial :
            return True
        else :
            return False

motDePasse = "Test124!"

print(valider_mot_de_passe(motDePasse))