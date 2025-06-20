# Getpass permet de cacher un message dans la console
import getpass
# random donne un nombre aléatoire dans un intervalle
from random import randint

# L'autre fonction erreur_saise n'est pas utilise à cause de getpass
def demander_valeur_cachee(joueur: str, min: int, max: int) -> int:
    """
    Demande à l'utilisateur de saisir une valeur masquée et vérifie qu'elle est comprise entre min et max.
    
    Paramètres :

        - joueur : Nom du joueur qui doit saisir la valeur.
        - min : Limite minimale .
        - max : Limite maximale.
    
    Retourne :

        - int : La valeur saisie et validée.

    """
    from Menu import couleur_affichage
    valeur : int

    while True:
        # Verifie ce qui est rentré dans la valeur a chercher
        try:
            valeur = int(getpass.getpass(couleur_affichage("vert",f"{joueur} : Saisissez une valeur (cachée) entre {min} et {max} : ")))
            
            # Si la valeur est comprise entre min et max alors elle est validé et renvoyé
            if min < valeur and valeur < max:
                return valeur
            
            else:
                print(couleur_affichage("rouge",f"⚠️  Erreur : La valeur doit être comprise entre {min} et {max}."))
        
        except ValueError:
            print(couleur_affichage("rouge","⚠️  Erreur : Vous devez entrer un nombre entier valide."))


def diff_niveau(minimum : int, maximum : int, tentative : int, niveau : int) -> int|None:
    """
    Cette fonction joue en fonction du niveau du robot
    
    Niveau 1 : Le robot va jouer aléatoirement

    Niveau 2 : Il utilise la méthode dichotomique et pour le dernier coup
    il va propose un nombre aléatoire

    Niveau 3 : Joue de manière dichotomique avec 7 tentatives donc il gagnera tout le temps

    Paramètre : 

        - minimum (int) : L'intervalle inférieur
        - maximal (int) : L'intervalle supérieur
        - tentative (int) : Le nombre de tentatives restantes
        - niveau (int) : Le niveau du robot

    Retourne :

        - int|None : Retourne le nombre proposé par le robot
        
    """
    milieu : float

    if niveau == 1:
        return randint(minimum, maximum)
    
    elif niveau == 2:

        if tentative != 1 :
            milieu = (maximum+minimum)/ 2
        else :
            milieu = randint(minimum,maximum)
        return int(milieu)
    
    elif niveau == 3:
        milieu = (maximum+minimum)/ 2
        return int(milieu)


def robot(niveau: int, tentative: int, nombre_cherche : int, joueur1 :str , joueur2 :str,quiJoue : int) -> tuple[int|None,int,int]:
    """
    Fonction qui s'occupe de gérer les robots en fonction du niveau demandé

    Paramètre :

        - niveau (int) : Le niveau du robot
        - tentative (int) : Le nombre de tentatives restantes
        - nombre_chercher (int) : Le nombre qui doit être trouvé
        - joueur1 (str) : Le nom du joueur 1
        - joueur2 (str) : Le nom du joueur 2
        - quiJoue (int) : Le joueur qui joue

    Retourne : 

        - tuple[int,int,int] : renvoie le nombre de tentative le nombre propose et le nombre cherche

    """
    from Menu import couleur_affichage
    import time

    minimum : int
    maximum : int
    nombre_propose : int|None

    minimum = 0
    maximum = 100

    if niveau == 1:
        print(couleur_affichage("vert", "Ce robot est facile à battre donc au lieu d'avoir 5 tentatives, il en a 7."))
        tentative = 6

    elif niveau == 2 :
        tentative = 4

    else :
        tentative = 6
        print(couleur_affichage("vert", "Ce robot à 7 tentatives pour trouver le nombre cherché"))
        print(couleur_affichage("vert","Ce robot est impossible à battre s'il cherche le nombre"))

    nombre_propose = diff_niveau(minimum,maximum,tentative,niveau)

    print(couleur_affichage("jaune", f"{joueur1 if quiJoue == 1 else joueur2} réfléchi ..."))

            
    while nombre_propose != nombre_cherche and tentative != 0:

        time.sleep(1.5)

        if nombre_propose != None:
                
            if nombre_propose < nombre_cherche:

                minimum = max(minimum, nombre_propose)

                print(couleur_affichage("jaune", f"Le nombre proposé est {nombre_propose}"))
                print(couleur_affichage("vert", "🔼 Trop petit !"))

                nombre_propose = diff_niveau(minimum + 1, maximum - 1, tentative, niveau)

            elif nombre_propose > nombre_cherche:

                maximum = min(maximum, nombre_propose)

                print(couleur_affichage("jaune", f"Le nombre proposé est {nombre_propose}"))
                print(couleur_affichage("vert", "🔽 Trop grand !"))

                nombre_propose = diff_niveau(minimum + 1, maximum - 1, tentative, niveau)

        tentative -= 1
        
    if nombre_propose == nombre_cherche and tentative != 0:
        time.sleep(1.5)
        print(couleur_affichage("jaune", f"Le nombre proposé par le {joueur1 if quiJoue == 1 else joueur2} est {nombre_propose}"))
    
    else:
        time.sleep(1.5)
        print(couleur_affichage("jaune", f"Le nombre proposé par le {joueur1 if quiJoue == 1 else joueur2} est {nombre_propose}"))
    
    return nombre_propose,nombre_cherche,tentative
        

def devinette(joueur1: str, joueur2: str,niveau : int, tours : int, quiJoue : int) -> str:

    
    from Menu import erreur_entree,changer_joueur,couleur_affichage,contient_robot

    """
    Lance une partie du jeu de devinette où les joueurs s'alternent pour choisir un nombre et deviner celui de l'autre.

    Paramètres:

        - joueur1 : Nom du joueur 1.
        - joueur2 : Nom du joueur 2.
        - niveau : Le niveau des robots
        - tours : Nombre de tours à jouer.
        - quiJoue : Joueur qui va jouer

    Retourne:

        - str: Le nom du gagnant.

    """
    nombre_cherche: int
    nombre_propose: int|None
    resultatjoueur1: int
    resultatjoueur2: int
    tentative: int
    joueur_eq_bot : bool

    print(couleur_affichage("blanc",f"Vous allez donc jouer pendant {tours} tours \n"))

    resultatjoueur1 = 0
    resultatjoueur2 = 0

    # Cette boucle vérifie si un des joueurs a gagné
    while resultatjoueur1 != tours and resultatjoueur2 != tours:
        
        if niveau == 1 or niveau == 3:
            tentative = 6
        else :
            tentative = 4

        # Valeur cachée par la bibliothèque getpass et vérifie l'entrée de l'utilisateur
        if quiJoue == 1 and contient_robot(joueur1) == False:
            nombre_cherche = demander_valeur_cachee(joueur1, 0, 100)
        elif quiJoue == 2 and contient_robot(joueur2) == False :
            nombre_cherche = demander_valeur_cachee(joueur2, 0, 100)
        else: 
            nombre_cherche = randint(0,100)
            print(couleur_affichage("vert",f"{joueur1 if quiJoue == 1 else joueur2} : Saisissez une valeur (cachée) entre 0 et 100 :"))

        print(couleur_affichage("vert",f"{joueur1 if quiJoue == 1 else joueur2} a bien saisi une valeur \n"))


        # Change le joueur qui joue
        quiJoue = changer_joueur(quiJoue)


        # Demande une valeur au joueur qui cherche le nombre et ensuite contrôle le nombre
        print(couleur_affichage("bleu",f"Au tour de {joueur1 if quiJoue==1 else joueur2}\033[0m \n"))


        # Vérifie si un des deux joueurs est un robot
        if contient_robot(joueur1) and quiJoue == 1:
            nombre_propose = -1
            joueur_eq_bot = True

        elif contient_robot(joueur2) and quiJoue == 2:
            nombre_propose = -1
            joueur_eq_bot = True

        else:
            joueur_eq_bot = False
            nombre_propose = erreur_entree(0, 100, couleur_affichage("vert",f"{joueur1 if quiJoue == 1 else joueur2} : Vous avez {tentative + 1} tentatives pour trouver le nombre, saisissez votre valeur : "),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier "),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier compris entre 0 et 100"))


        # Regarde si le nombre entré par l'utilisateur et le nombre gagnant et agit en fonction (trop petit, trop grand)
        while nombre_cherche != nombre_propose and tentative != 0:

            if joueur_eq_bot == True :

                nombre_propose,nombre_cherche,tentative = robot(niveau,tentative,nombre_cherche,joueur1,joueur2,quiJoue)

            else :
                
                if nombre_propose != None :
                    if nombre_cherche > nombre_propose:
                        tentative -= 1
                        nombre_propose = erreur_entree(0, 100, couleur_affichage("vert",f"🔼 Trop petit ! {joueur1 if quiJoue == 1 else joueur2}, vous devez essayer une autre valeur : "),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier"),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier compris entre 0 et 100 \033[0m"))

                    elif nombre_cherche < nombre_propose:
                        tentative -= 1
                        nombre_propose = erreur_entree(0, 100, couleur_affichage("vert",f"🔽 Trop grand ! {joueur1 if quiJoue == 1 else joueur2} vous devez essayer une autre valeur : "),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier "),couleur_affichage("rouge","⚠️  La valeur doit être un nombre entier compris entre 0 et 100"))

        print(couleur_affichage("vert",f"\nLe nombre cherché était {nombre_cherche}"))

        if tentative == 0 and nombre_cherche != nombre_propose:

            print(couleur_affichage("jaune","\n📋 Vous avez fait trop tentatives sans trouver le nombre, c'est maintenant à l'autre joueur de jouer \n\033[0m"))

            if quiJoue == 1:
                resultatjoueur2 += 1
            else:
                resultatjoueur1 += 1

        else:
            print(couleur_affichage("jaune","\n🏆 Vous avez trouvé le bon nombre, BRAVO !!!\n"))

            # Augmente les scores en fonction des parties gagnées
            if quiJoue == 1:
                resultatjoueur1 += 1
            else:
                resultatjoueur2 += 1

        print(couleur_affichage("magenta",f"Voici le résultat de {joueur1} : "), resultatjoueur1)
        print(couleur_affichage("cyan",f"Voici le résultat de {joueur2} : "), resultatjoueur2, "\n")

    if resultatjoueur1 == tours:
        print(couleur_affichage("jaune",f"🎉 {joueur1} a gagné la partie 🎉"))
        return joueur1
    else:
        print(couleur_affichage("jaune",f"🎉 {joueur2} a gagné la partie 🎉"))
        return joueur2