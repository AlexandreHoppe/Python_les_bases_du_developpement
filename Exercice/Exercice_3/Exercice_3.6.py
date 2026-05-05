# Créez un programme qui génère des citations aléatoires à partir d'un nombre aléatoire. L'utilisateur devrait pouvoir
# choisir un thème et le programme générera une citation aléatoire correspondante. Utilisez des correspondances pour
# gérer les différents thèmes et générer les citations appropriées.

import random
import os


nombreCitations = random.randint(1, 10)
themeVoulus = int(input("Quelle thème : \n1. Répliques de jeux vidéo \n2.Répliques de films\n3.Répliques de série \n "))

match themeVoulus :
    case 1 : 
        match nombreCitations :
            case 1 :
                print("'It's me, Mario.' Super Mario 64")
            case 2 :
                print("'Le mur je te présente le visage, le visage je te présente le mur.' Splinter Cell Conviction")
            case 3 :
                print("'Tout le monde pense être le héros de sa propre histoire.' Borderlands")
            case 4 :
                print("'Moi aussi j'étais un aventurier autrefois, et puis j'ai pris une flèche dans le genou.' Skyrim")
            case 5 :
                print("'Wololoooo!' Age Of Empire II")
            case 6 :
                print("'La bonne personne au mauvais endroit peut faire toute la différence.' Half-Life 2")
            case 7 :
                print("'Nous faisons tous des choix, mais en réalité, ce sont ces choix qui nous font.' Bioshock")
            case 8 :
                print("'Tu veux qu'on se tire l'oreille ?' Metal Gear Solid")
            case 9 :
                print("'Vous, vous êtes soit incroyablement courageux, soit immensément con !' Mass Effect 2")
            case 10 :
                print("'Mes pieds je les mets où je veux et souvent dans la gueule.' Mass Effect")

    case 2 : 
        match nombreCitations :
            case 1 :
                print("'Je suis fatigué patron, fatigué de devoir courir les routes et d'être seul comme un moineau sous la pluie. Fatigué d'avoir jamais un ami pour parler, pour me dire où on va, d'où on vient et pourquoi. Mais surtout je suis fatigué de voir les hommes se battre les uns les autres, je suis fatigué de toute la peine et la souffrance que je sens dans le monde.' La Ligne Verte")
            case 2 :
                print("'Messire, messire, un sarrasin dans une charriote du diable ! c'est tout ferré y'a point d'boeuf pour tirer !' Les visiteurs")
            case 3 :
                print("'Tu vois, le monde se divise en deux catégories, ceux qui ont un pistolet chargé et ceux qui creusent. Toi, tu creuses.' Le bon, la brute et le truand")
            case 4 :
                print("'Mon nom est Maximus Desimus Meridius, commandant en chef des armées du nord, général des légions Félix, fidèle serviteur du vrai empereur Marc Aurel. Père d'un fils assassiné, époux d'une femme assassiné, et j'aurais ma vengeance dans cette vie ou dans l'autre.' Gladiator")
            case 5 :
                print("'C'est trop calme. j'aime pas trop beaucoup ça. J'préfère quand c'est un peu trop plus moins calme.' Astérix et Obélix : mission Cléopâtre")
            case 6 :
                print("'Si tu veux un conseil, oublie que t'as aucune chance. On sait jamais, sur un malentendu ça peut marcher.' Les bronzés font du ski")
            case 7 :
                print("'Je sais que je plais pas à tout le monde... Mais quand je vois à qui je plais pas, je m'demande si ça me dérange vraiment.' Dikkenek")
            case 8 :
                print("'Ce que j'ai subi a fait de moi ce que je suis.' V pour Vendetta")
            case 9 :
                print("'L'ennemi est dangereux Maverick, mais toi, t'es pire que l'ennemi... tu es dangereux et con !' Top gun")
            case 10 :
                print("'- Il s'appelle Juste Leblanc. - Ah bon, il n'a pas de prénom ?- Je viens de vous le dire Juste Leblanc. Votre prénom c'est François, c'est juste ? Eh bien lui c'est pareil, c'est Juste. - .' Le dîner de cons")

    case 3 : 
        match nombreCitations :
            case 1 :
                print("'C'est difficile de mettre une laisse à un chien une fois qu'on lui a posé une couronne sur la tête.' Game of Thrones")
            case 2 :
                print("'L'Amour prend patience, il est plein de bonté. L'amour n'est point envieux ; l'amour ne se vante point, n'est pas irrespectueux, il ne cherche point son intérêt, il ne s'irrite point, il ne soupçonne point le mal. L'amour pardonne tout, il croit tout, il espère tout, il supporte tout.' How I Met Your Mother")
            case 3 :
                print("'Le chaos n'est pas une fosse, le chaos est une échelle. Seule l'échelle est réelle. Seule l'ascension importe.' Game of Thrones")
            case 4 :
                print("'Imagine que Martin Luther King est dit : 'J'ai fait un rêve... mais j'ai pas envie d'en parler'.' Friends")
            case 5 :
                print("'La plupart des gens disent qu'on a besoin d'amour pour vivre. En fait, on a surtout besoin d'oxygène.' Docteur House")
            case 6 :
                print("'Si vous parlez à dieu, vous êtes croyant. S'il vous répond c'est que vous êtes schyzo.' Docteur House")
            case 7 :
                print("'- Qu'allez-vous faire ? - Je me disais que j'allais écouter vos théories, les rejeter, puis ne garder que la mienne. Comme d'habitude.' Docteur House")
            case 8 :
                print("'Je suis occupé. En fait comme vous le voyez je ne suis pas occupé, c'est une façon polie de vous dire de dégager.' Docteur House")
            case 9 :
                print("'- Qu'est-ce qui est petit et marron ? - Un marron ! - Putain il est fort, ce con.' Kaamelott")
            case 10 :
                print("'Il n'y a pas de repos pour moi dans ce monde. Peut-être dans le prochain!' Peaky Blinders")