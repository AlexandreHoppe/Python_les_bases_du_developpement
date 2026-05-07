# Invitez l'utilisateur à saisir son prénom et son nom. Ensuite, créez un tuple contenant ces informations. Pour finir,
# affichez séparément le prénom et le nom à partir du tuple.

tupleUtilisateur = tuple()
tupleUtilisateur = (input("Entrez votre prenom : "), input("Entrez votre nom : ") )

print(tupleUtilisateur[0], tupleUtilisateur[1], sep='     ')