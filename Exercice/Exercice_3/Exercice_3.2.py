# Créez un programme qui convertit une note numérique en une note alphabétique en utilisant une échelle de notation
# standard. Utilisez des correspondances pour déterminer la note alphabétique correspondante en fonction de la note
# numérique.

noteNumérique = int(input("Entrez la note à convertir : "))

if noteNumérique > 100 or noteNumérique < 0 :
    print("Note invalide")
elif noteNumérique <= 100 and noteNumérique >= 94 :
    print('A')
elif noteNumérique >= 90 :
    print('A-')
elif noteNumérique >= 87 :
    print('B+')
elif noteNumérique >= 84 :
    print('B')
elif noteNumérique >= 80 :
    print('B-')
elif noteNumérique >= 77 :
    print('C+')
elif noteNumérique >= 74 :
    print('C')
elif noteNumérique >= 70 :
    print('C-')
elif noteNumérique >= 67 :
    print('D+')
elif noteNumérique >= 64 :
    print('D')
elif noteNumérique >= 60 :
    print('D-')
elif noteNumérique >= 0 :
    print('F')
  
    