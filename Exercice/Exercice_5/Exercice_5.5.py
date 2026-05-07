# Créez une liste de tuples contenant le nom et l'âge de trois personnes. Trouvez ensuite la personne la plus âgée et
# affichez son nom.

tupleUn = tuple
tupleUn = ("Bob", 34)
tupleDeux = ("Steve", 40)
tupleTrois = ("John", 39)
tupleIndex = 0
tupleAge = 0

listeTuple = [tupleUn, tupleDeux, tupleTrois]

for x in range(len(listeTuple)) :
    if listeTuple[x][1] > tupleAge :
        tupleAge = listeTuple[x][1]
        tupleIndex = x

print(listeTuple[tupleIndex][0])