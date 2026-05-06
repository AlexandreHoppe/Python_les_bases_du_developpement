# Concevez un programme qui génère et affiche les nombres premiers jusqu'à 100 en utilisant une boucle.

for x in range(1, 100, 1) :
    modZero = 0
    for y in range(1, 10, 1) :
        if x % y == 0 :
            modZero = modZero + 1
            #print(x, y, modZero, sep='     ')
    
    if modZero == 2 and x < 10:
        print(x)
    elif modZero < 2 and x > 10 :
        print(x)

    
