
"""Import des bibliothèques"""
from typing import TextIO#import du type TextIO depuis le module typing
import os #import du module os
import json #import du module json
from random import randint #import du module randint
import importlib
################################################################



def contient_robot(texte: str) -> bool:
    """
    Vérifie si le texte contient le mot 'robot' ou une partie de mot contenant 'robot'.

    Paramètre :
   
        - texte (str) : La chaîne de caractères à vérifier.

    Retourne :

        - bool : True si 'robot' est présent, False sinon.

    """

    return "robot" in texte.lower()


def pileouface(joueur1 : str,joueur2 : str) -> tuple[str,str,int]:
    """
    Permet d'effectuer un pile ou face et ainsi de donner la main au joueur remportant le pile ou face

    Paramètres : 

        - joueur1 (str) : nom du joueur 1
        - joueur2 (str) : nom du joueur 2

    Retourne :

        - Tuple(str,str,int) : La fonction retourne le nom du joueur1 et du joueur2, ainsi que 1 pour savoir quijoue

    """

    pileouface : int
    choixjoueur1 : int
    tmp = str

    tmp = ""

    choixjoueur1 = 0

    if contient_robot(joueur1):
        choixjoueur1 = int(randint(1,2))
        if choixjoueur1 == 1:
            print(" ")
            print(couleur_affichage("cyan",f"{joueur1} a choisi pile !"))
        else:
            print(" ")
            print(couleur_affichage("cyan",f"{joueur1} a choisi face !"))
    else:
        choixjoueur1 = erreur_entree(1,2,couleur_affichage("cyan","Saississer 1 pour pile ou 2 pour face : "),
                                     couleur_affichage("rouge", "❌ La valeur saisie doit être un nombre entier positif."),
                                     couleur_affichage("rouge", "⚠️  La valeur doit être un entier compris entre 1 et 2."))

    pileouface = int(randint(1,2))

    if pileouface == 1:
        print(" ")
        print(couleur_affichage("bleu","La pièce est retomber sur pile !"))
    else: 
        print(" ")
        print(couleur_affichage("bleu","La pièce est retomber sur face !"))
    
    if pileouface == choixjoueur1:
        print(" ")
        print(couleur_affichage("cyan",f"{joueur1} à la main !"))
    else:
        print(" ")
        print(couleur_affichage("cyan",f"{joueur2} à la main !"))
        tmp = joueur1
        joueur1 = joueur2
        joueur2 = tmp

    
    print(" ")
    print(couleur_affichage("magenta",f"Le joueur 1 est : {joueur1}"))
    print(couleur_affichage("magenta",f"Le joueur 2 est : {joueur2}"))

    return joueur1,joueur2,1
    


def conversion_chiffrelettre(choix : str,message : str) -> int:
    """
    Cette fonction permet de convertir un nombre en toute lettres en un nombre en chiffre

    Paramètres :

        - choix (str) : chaîne de caractère qui est le choix donné par l'utilisateur
        - message (str) : Message pour utilisateur

    Retourne : 

        - int

    """

    dictionnairenombrelettre : dict[str,int]
    dictionnairenombrelettreentier : dict[str,int]
    chiffres : str
    nombre : str
    tourne : bool

    dictionnairenombrelettre = {
    "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9,
    "dix": 10, "onze": 11, "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16, "dix sept": 17,
    "dix huit": 18, "dix neuf": 19, "vingt": 20, "vingt et un": 21, "vingt deux": 22, "vingt trois": 23,
    "vingt quatre": 24, "vingt cinq": 25, "vingt six": 26, "vingt sept": 27, "vingt huit": 28, "vingt neuf": 29,
    "trente": 30, "trente et un": 31, "trente deux": 32, "trente trois": 33, "trente quatre": 34, "trente cinq": 35,
    "trente six": 36, "trente sept": 37, "trente huit": 38, "trente neuf": 39, "quarante": 40, "quarante et un": 41,
    "quarante deux": 42, "quarante trois": 43, "quarante quatre": 44, "quarante cinq": 45, "quarante six": 46,
    "quarante sept": 47, "quarante huit": 48, "quarante neuf": 49, "cinquante": 50, "cinquante et un": 51,
    "cinquante deux": 52, "cinquante trois": 53, "cinquante quatre": 54, "cinquante cinq": 55, "cinquante six": 56,
    "cinquante sept": 57, "cinquante huit": 58, "cinquante neuf": 59, "soixante": 60, "soixante et un": 61,
    "soixante deux": 62, "soixante trois": 63, "soixante quatre": 64, "soixante cinq": 65, "soixante six": 66,
    "soixante sept": 67, "soixante huit": 68, "soixante neuf": 69, "soixante dix": 70, "soixante et onze": 71,
    "soixante douze": 72, "soixante treize": 73, "soixante quatorze": 74, "soixante quinze": 75, "soixante seize": 76,
    "soixante dix sept": 77, "soixante dix huit": 78, "soixante dix neuf": 79, "quatre vingt": 80, "quatre vingt un": 81,
    "quatre vingt deux": 82, "quatre vingt trois": 83, "quatre vingt quatre": 84, "quatre vingt cinq": 85,
    "quatre vingt six": 86, "quatre vingt sept": 87, "quatre vingt huit": 88, "quatre vingt neuf": 89,
    "quatre vingt dix": 90, "quatre vingt onze": 91, "quatre vingt douze": 92, "quatre vingt treize": 93,
    "quatre vingt quatorze": 94, "quatre vingt quinze": 95, "quatre vingt seize": 96, "quatre vingt dix sept": 97,
    "quatre vingt dix huit": 98, "quatre vingt dix neuf": 99, "cent": 100
}


    dictionnairenombrelettreentier = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16, "17": 17, "18": 18, "19": 19, "20": 20,
    "21": 21, "22": 22, "23": 23, "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30,
    "31": 31, "32": 32, "33": 33, "34": 34, "35": 35, "36": 36, "37": 37, "38": 38, "39": 39, "40": 40,
    "41": 41, "42": 42, "43": 43, "44": 44, "45": 45, "46": 46, "47": 47, "48": 48, "49": 49, "50": 50,
    "51": 51, "52": 52, "53": 53, "54": 54, "55": 55, "56": 56, "57": 57, "58": 58, "59": 59, "60": 60,
    "61": 61, "62": 62, "63": 63, "64": 64, "65": 65, "66": 66, "67": 67, "68": 68, "69": 69, "70": 70,
    "71": 71, "72": 72, "73": 73, "74": 74, "75": 75, "76": 76, "77": 77, "78": 78, "79": 79, "80": 80,
    "81": 81, "82": 82, "83": 83, "84": 84, "85": 85, "86": 86, "87": 87, "88": 88, "89": 89, "90": 90,
    "91": 91, "92": 92, "93": 93, "94": 94, "95": 95, "96": 96, "97": 97, "98": 98, "99": 99, "100": 100
}


    nombre = ""
    tourne = True
       
    while tourne:
        
        for chiffres in dictionnairenombrelettre:
            if chiffres == choix:
                nombre = choix
        
        for chiffres in dictionnairenombrelettreentier:
            if chiffres == choix:
                nombre = choix
        
        if nombre != choix:
            print(couleur_affichage("rouge","❌ Vous n'avez pas saisie la bonne valeur, recommencez ! "))
            choix = str(input(message))
            tourne = True
        else:
            tourne = False



    if nombre in dictionnairenombrelettre :
        return int(dictionnairenombrelettre[nombre])
    else:
        return int(dictionnairenombrelettreentier[nombre])


def nombre_tours() -> int:
    """
    Fonction qui demande le nombre de parties que les joueurs veulent faire et compte 
    le nombre de tours nécessaires pour qu'un gagnant soit désigné.

    Paramètre :

        - Rien
    
    Retourne:

        - int : retourne le nombre de tours

    """
    tours: int
    tours = erreur_entree(1, 20, couleur_affichage("cyan", "➡️  Combien de parties souhaitez-vous jouer ? (1 à 20) : "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"),couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 20."))

    while tours % 2 != 1:
        tours = erreur_entree(1, 20,couleur_affichage("cyan", "➡️  Le nombre de parties doit être impair pour qu'il y ait un gagnant (1 à 20) : "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"),couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 20."))

    if tours == 1:
        return tours
    else:
        return (tours // 2 + 1)


def changer_joueur(quiJoue: int) -> int:
    """
    Change le joueur qui doit jouer.

    Paramètre:
    
        - quiJoue : Identifiant du joueur actuel (1 ou 2).

    Retourne:
    
        - int: L'identifiant du prochain joueur (2 si c'était 1, ou 1 si c'était 2).
    """
    return 2 if quiJoue == 1 else 1

    
def couleur_affichage(couleur: str, texte: str) -> str:
    """
    Fonction qui permet de mettre un texte en couleur dans la console

    Paramètres : 

        - couleur : prend la couleur souhaité
        - texte : prend le texte qui doit être affiché en couleur

    Retourne :

        - str : retourne le texte dans la couleur demandé, si couleur introuvable
        alors elle l'affiche en blanc

    """
    if couleur == "rouge":
        return f"\033[31m{texte}\033[0m"
    elif couleur == "vert":
        return f"\033[32m{texte}\033[0m"
    elif couleur == "jaune":
        return f"\033[33m{texte}\033[0m"
    elif couleur == "bleu":
        return f"\033[34m{texte}\033[0m"
    elif couleur == "magenta":
        return f"\033[35m{texte}\033[0m"
    elif couleur == "cyan":
        return f"\033[36m{texte}\033[0m"
    elif couleur == "blanc":
        return f"\033[37m{texte}\033[0m"
    elif couleur == "gris":
        return f"\033[90m{texte}\033[0m"
    elif couleur == "orange":
        return f"\033[38;5;208m{texte}\033[0m"
    elif couleur == "rose":
        return f"\033[38;5;200m{texte}\033[0m"
    elif couleur == "violet":
        return f"\033[38;5;93m{texte}\033[0m"
    elif couleur == "turquoise":
        return f"\033[38;5;14m{texte}\033[0m"
    elif couleur == "or":
        return f"\033[38;5;220m{texte}\033[0m"
    elif couleur == "argent":
        return f"\033[38;5;250m{texte}\033[0m"
    else:
        return f"\033[37m{texte}\033[0m"

    
def proposition() -> None:
    """
    Fonction qui sert à afficher les jeux avec un affichage séparé de '#' et un menu qui est proposé.

    Paramètre :

        - Rien

    Retourne : 

        - Rien

    """

    print(couleur_affichage("gris", "-" * 50))
    print(couleur_affichage("rose", "🎯 1. Devinette"))
    print(" ")
    print(couleur_affichage("jaune", "🔥 2. Allumettes"))
    print(" ")
    print(couleur_affichage("cyan", "❌ 3. Morpion"))
    print(" ")
    print(couleur_affichage("vert", "📊 4. Afficher les scores"))
    print(" ")
    print(couleur_affichage("gris", "📃 5. Afficher les règles"))
    print(" ")
    print(couleur_affichage("bleu","🔄 6. Changez de mode de jeu"))
    print("")
    print(couleur_affichage("orange","⚙️  7. Modifier la difficulté"))
    print(" ")
    print(couleur_affichage("rouge", "⛔ 8. Quitter"))
    print(couleur_affichage("gris", "-" * 50))
    

def proposition_difficulte() -> int:
    """
    Fonction qui affiche le niveau de difficulté souhaité

    Paramètre :

        - Rien

    Retourne :

        - int : Choix de l'utilisateur entre difficile, moyen, et  facile

    """
    entree_utilisateur : int

    print(couleur_affichage("cyan","Il existe 3 niveaux de difficulté"))
    print("")
    print(couleur_affichage("cyan","    - 1. Facile (Si vous gagnez cela vous rapportera moins de points)"))
    print(couleur_affichage("cyan","    - 2. Moyen (Si vous gagnez cela vous rapportera plus de points que le niveau facile)"))
    print(couleur_affichage("cyan","    - 3. Difficile (Si vous gagnez cela vous rapportera plus de points) \n"))

    entree_utilisateur = erreur_entree(1,3,couleur_affichage("cyan","➡️  Quelle difficulté choisissez vous? : "),
                                       couleur_affichage("rouge","❌ La valeur entrée doit être un entier positif"),
                                       couleur_affichage("rouge","❌ La valeur doit être comprise entre 1 et 3"))
    
    
    return entree_utilisateur


def proposition_robot_joueur() -> int :
    """
    Fonction qui demande contre qui le joueur veut jouer

        - 1 : joueur
        - 2 : robot
    
    Retourne :

        - int : le choix du joueur

    """
    choix : int

    print(couleur_affichage("cyan","Les différents modes de jeu : \n"))
    print(couleur_affichage("cyan","    - 1 : Joueur contre Joueur"))
    print(couleur_affichage("cyan","    - 2 : Joueur contre Robot"))
    print(couleur_affichage("cyan","    - 3 : Robot contre Robot\n"))
    
    choix = erreur_entree(1,3,couleur_affichage("cyan","➡️  Quelle est votre choix (1,2 ou 3) : "),
    couleur_affichage("rouge","❌  Il faut soit rentrer 1 pour Joueur/Joueur, 2 pour Joueur/Robot ou 3 pour Robot/Robot"),
    couleur_affichage("rouge","❌  Vous avez dépassé la limite il faut soit rentrer un ou trois"))

    return choix


def reglejeu() -> None:
    """
    Fonction qui sert à afficher les règles des jeux avec un affichage en fonction du choix fait dans la fonction menu.

    Paramètres :

        - Rien
    
    Retourne :

        - Rien

    """

    choix : int
    souhait : str
    quitter : bool

    quitter = True

    while quitter:
        choix = erreur_entree(1,5,couleur_affichage("magenta","Quel règles souhaitez vous afficher, 1 pour devinette, 2 pour allumettes, 3 pour morpion, 4 pour afficher le nombre de points remporté par difficulté et 5 pour quitter le menu des règles : "),couleur_affichage("rouge","Vous n'avez pas rentré la bonne valeur"),couleur_affichage("rouge","Vous n'avez pas choisi le bon chiffre"))
        match choix :
            case 1:
                print("")
                print(couleur_affichage("cyan","Voici les règles du jeu de la devinette."))
                print("")
                print(couleur_affichage("cyan","Un des deux joueurs choisit un nombre entre 0 à 100 (l'affichage du nombre choisit sera caché)."))
                print(couleur_affichage("cyan","Ensuite, le second joueur doit trouver le nombre choisit par le premier, il aura 5 tentatives."))
                print(couleur_affichage("cyan","Bien sur le joueur cherchant le nombre caché sera aider par des 'trop petit', 'trop grand' en fonction du nombre donné par le second joueur."))
                print("")

            case 2:
                print("")
                print(couleur_affichage("cyan","Voici les règles du jeu des allumettes."))
                print("")
                print(couleur_affichage("cyan","On dispose d'un tas de 20 allumettes."))
                print(couleur_affichage("cyan","Chaque joueur à tour de rôle en prélève 1,2 ou 3."))
                print(couleur_affichage("cyan","Le perdant est celui que prend la dernière allumettes."))
                print("")

            case 3:
                print("")
                print(couleur_affichage("cyan","Voici les règles du jeu du morpion."))
                print("")
                print(couleur_affichage("cyan","Ce jeu se déroule sur une grille de 3x3."))
                print(couleur_affichage("cyan","Chaque joueur à tour de rôle pose sa marque, soit 'o' soit 'x'."))
                print(couleur_affichage("cyan","Le gagnant est celui qui aligne 3 marques."))
                print("")
            
            case 4:
                print(" ")
                print(couleur_affichage("cyan","Voici le nombre de points remportés en fonction de la difficulté : "))
                print(" ")
                print(couleur_affichage("cyan","    - La difficulté facile vous rapporte 1 point"))
                print(couleur_affichage("cyan","    - La difficulté moyen vous rapporte 2 point"))
                print(couleur_affichage("cyan","    - La difficulté difficile vous rapporte 5 point"))
                print(" ")

            case 5:
                souhait = erreur_entree_str(["o", "oui", "non", "n"], couleur_affichage("magenta", "🚪 Souhaitez-vous quitter ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))
                if souhait in ["o", "oui"]:
                    print("")
                    print(couleur_affichage("jaune", "👋 Vous avez quitter le menu des règles !"))
                    quitter = False
                    
            case _:
                print(couleur_affichage("rouge", "❌ Choix invalide !!!"))


def menu(joueur1: str, joueur2: str,niveau : int, choix_mode : int) -> None:
    """
    Menu principal qui demande à l'utilisateur quelle jeu veut-il faire.

    Paramètre :

        - joueur1 (str) : Nom du joueur 1
        - joueur2 (str) : Nom du joueur 2
        - niveau (int) : niveau des ou du robot
        - choix_mode (int) : choix du mode de jeu

    Retourne :

        - Rien

    """
    choix: int
    quitter: bool
    joueurgagnant : str
    souhait: str
    tours: int
    jeu : str

    choix = 0
    quitter = True
    quiJoue = tuple[str,str,int]

    while quitter:

        quiJoue = pileouface(joueur1,joueur2)

        joueur1 = quiJoue[0]
        joueur2 = quiJoue[1]

        # Fonction qui affiche les différents jeu et fonctionnalité du menu
        print(" ")
        proposition()

        # Vérification de la valeur entrée par l'utilisateur (compris entre les limites et que la valeur est un nombre entier)
        print(" ")
        choix = erreur_entree(1, 8, couleur_affichage("magenta", "📝 Veuillez faire votre choix (1,2,3,4,5,6,7,8) : "),couleur_affichage("rouge", "❌ La valeur saisie doit être un nombre entier positif."),couleur_affichage("rouge", "⚠️  La valeur doit être un entier compris entre 1 et 8."))
        print(" ")
        

        match choix:

            case 1:
                # Jeu choisi est Devinette ()
                print(couleur_affichage("bleu", "🎯 Vous avez choisi le jeu de la Devinette !"))
                jeu = "devinette"
                tours = nombre_tours()
                joueurgagnant = devinette(joueur1,joueur2,niveau,tours,quiJoue[2])

                ajout_score("Scores.json",joueur1,joueur2,joueurgagnant,jeu,niveau)


            case 2:
                # Jeu choisi est Allumettes (choix 2)
                print(couleur_affichage("jaune", "🔥 Vous avez choisi le jeu des Allumettes !"))
                jeu = "allumettes"

                tours = nombre_tours()
                joueurgagnant = allumettes(joueur1,joueur2,niveau,tours,quiJoue[2])

                ajout_score("Scores.json",joueur1,joueur2,joueurgagnant,jeu,niveau)


            case 3:
                # Jeu choisi est Morpion (choix 3)
                print(couleur_affichage("cyan", "❌ Vous avez choisi le jeu du Morpion !"))
                jeu = "morpion"

                tours = nombre_tours()
                joueurgagnant = morpion(joueur1,joueur2,niveau,tours,quiJoue[2])

                ajout_score("Scores.json",joueur1,joueur2,joueurgagnant,jeu,niveau)


            case 4:
                # Affichage des scores (choix 4)
                print(couleur_affichage("vert", "📊 Vous avez choisi d'afficher les scores ! \n"))
                afficherscore(joueur1,joueur2)


            case 5:
                #Affichage des règles (choix 5)
                print("")
                reglejeu()


            case 6:
                # Modifier le mode de jeu
                choix_mode = proposition_robot_joueur()
                joueur1,joueur2,niveau = adaptation(choix_mode)
                print(couleur_affichage("cyan","Mode de jeu changé en : "))
                if choix_mode == 1:
                    print(" ")
                    print(couleur_affichage("cyan","Joueur contre Joueur"))
                    print(" ")
                    print(couleur_affichage("cyan","Les joueurs sont : "))
                    print(couleur_affichage("cyan",f"    - {joueur1} : joueur 1"))
                    print(couleur_affichage("cyan",f"    - {joueur2} : joueur 2"))
                elif choix_mode == 2:
                    print(" ")
                    print(couleur_affichage("cyan","Joueur contre Robot"))
                    print(" ")
                    print(couleur_affichage("cyan",f"Le joueur est : {joueur1} (joueur 1)"))
                    print(" ")
                    print(couleur_affichage("cyan",f"Et le robot est de difficulté : {joueur2} (joueur 2)"))
                else:
                    print(" ")
                    print(couleur_affichage("cyan","Robot contre Robot"))
                    print(" ")
                    print(couleur_affichage("cyan","Les robots sont de difficultés : "))
                    print(" ")
                    print(couleur_affichage("cyan",f"    - {joueur1} : joueur 1"))
                    print(couleur_affichage("cyan",f"    - {joueur2} : joueur 2"))

                


            case 7:
                # Modifier la difficulté
                if choix_mode == 1:
                    print(couleur_affichage("rouge","❌ Impossible de changez de difficulté !"))
                    print(couleur_affichage("rouge","❌ Vous ne jouez contre aucun robot !"))
                else: 
                    niveau = proposition_difficulte()
                    print(" ")
                    print(couleur_affichage("bleu",f"Niveau de difficulté changé en : {niveau}"))


            case 8:
                # Demande de quitter le jeu
                souhait = erreur_entree_str(["o", "oui", "non", "n"], couleur_affichage("magenta", "🚪 Souhaitez-vous quitter ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))
                
                if souhait in ["o", "oui"]:
                    print(couleur_affichage("jaune", "👋 Merci de nous avoir utilisé !"))
                    quitter = False


            case _:
                print(couleur_affichage("rouge", "❌ Choix invalide !!!"))


def ajout_score(chemin_fichier : str, joueur1 : str, joueur2 : str, gagnant : str, jeu : str, niveau : int) -> None:
    """
    Modifie les scores si la partie existe déjà, sinon ajoute un score avec le gagnant et le jeu

    Paramètres :

        - chemin_fichier : str
        - joueur1 : str
        - joueur2 : str
        - gagnant : str
        - jeu : str
        - niveau : int

    Retourne :

        - Rien

    """

    
    cle_partie : str
    score_j1 : int
    score_j2 : int
    f : TextIO
    scoredesjoueurs : list[str]
    data : dict[str,dict[str,str]]



    try :
        if (not contient_robot(joueur1) and not contient_robot(joueur2)) or (not contient_robot(joueur1)) or (not contient_robot(joueur2)):
            if not os.path.exists(chemin_fichier):
                data = {}
                with open(chemin_fichier, 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                with open(chemin_fichier, 'r') as f:
                    data = json.load(f)

            cle_partie = f"{joueur1}-{joueur2}"

            if cle_partie not in data:
                data[cle_partie] = {}

            if jeu not in data[cle_partie]:
                data[cle_partie][jeu] = "0-0"

            score = data[cle_partie][jeu]

            scoredesjoueurs = score.split("-")

            score_j1 = int(scoredesjoueurs[0])
            score_j2 = int(scoredesjoueurs[1])

            if niveau == 3:  
                if gagnant == joueur1:
                    score_j1 += 5
                else:
                    score_j2 += 5
            elif niveau == 2:
                if gagnant == joueur1:
                    score_j1 += 2
                else:
                    score_j2 += 2
            else:
                if gagnant == joueur1:
                    score_j1 += 1
                else:
                    score_j2 += 1


            data[cle_partie][jeu] = f"{score_j1}-{score_j2}"

            with open(chemin_fichier, 'w') as f:
                json.dump(data, f, indent=4)
                print(couleur_affichage("magenta","Les scores ont bien étaient modifiés !"))
        else:
            print(" ")
            print(couleur_affichage("magenta","Nous n'ajouterons pas les scores puisque les deux joueurs sont des robots !"))

            
    except ValueError:
        print(couleur_affichage("rouge","Une erreur est survenue"))
        print(couleur_affichage("rouge","Le fichier est surement corrompu, supprimez le et le problème sera résolu"))


def afficherscore(joueur1 : str, joueur2 : str) -> None:
    """
    Sauvegarde les données des parties dans un fichier txt

    Paramètre :

        - joueur1 (str) : nom du joueur 1
        - joueur2 (str) : nom du joueur 2
    
    Retourne :

        - Rien

    """
    choix : int
    souhait : str
    quitter : bool
    cle_partie1 : str
    cle_partie2 : str
    affichage : str
    data : dict[str,dict[str,str]]
    data_triees : dict[str,dict[str,str]]
    f : TextIO 
    parties : str
    choixpartie : str
    trouve : bool


    trouve = False
    quitter = True

    try :

        while quitter:

            choix = erreur_entree(1,2,couleur_affichage("magenta","Choississez 1 pour afficher le score, 2 pour quitter : "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"),couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 20."))

            match choix:

                case 1:

                    affichage = erreur_entree_str(["oui","o","non","n"],couleur_affichage("magenta","Souhaitez vous afficher le score de la partie en cours ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))

                    with open("Scores.json", 'r') as f:
                        data = json.load(f)
                    
                    if affichage in ["oui","o"]:
                        print(" ")
                        cle_partie = f"{joueur1}-{joueur2}"
                        print(couleur_affichage("cyan",cle_partie))
                        parties = str(data[cle_partie])
                        print(couleur_affichage("cyan",parties))

                    else:
                        print(" ")
                        print(couleur_affichage("vert","Voici tous les scores triés par ordre alphabétique : "))
                        print(" ")

                        data_triees = dict(sorted(data.items()))

                        for parties in data_triees:
                            print(couleur_affichage("cyan",parties))
                            print(couleur_affichage("cyan",f"{data_triees[parties]}\n"))


                        input(couleur_affichage("magenta","Appuyer sur entrée . . ."))

                        choixpartie = erreur_entree_str(["o", "oui", "non", "n"], couleur_affichage("magenta", "🚪 Souhaitez-vous chercher une partie en particulier ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))
                        
                        if choixpartie in ["o","oui"]:
                            joueur1 = str(input(couleur_affichage("magenta","Quel est le nom d'un des joueurs de la partie ? : ")))
                            print(" ")

                            for parties in data_triees:
                                if joueur1 in parties:
                                    trouve = True
                                    print(couleur_affichage("cyan",parties))
                                    print(couleur_affichage("cyan",f"{data_triees[parties]}\n"))
                                    
                            if not trouve:
                                print(couleur_affichage("rouge","Aucunes parties n'a été trouvées !"))

                            choixpartie = erreur_entree_str(["o", "oui", "non", "n"], couleur_affichage("magenta", "🚪 Souhaitez-vous afficher une partie en particulier ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))

                            if choixpartie in ["oui","o"]:
                                
                                joueur2 = str(input(couleur_affichage("magenta","Quel est le nom du second joueur de la partie ? : ")))

                                cle_partie1 = f"{joueur1}-{joueur2}"
                                cle_partie2 = f"{joueur2}-{joueur1}"

                                if cle_partie1 in data_triees:
                                    print(couleur_affichage("cyan", cle_partie1))
                                    print(couleur_affichage("cyan", f"{data_triees[cle_partie1]}\n"))
                                elif cle_partie2 in data_triees:
                                    print(couleur_affichage("cyan", cle_partie2))
                                    print(couleur_affichage("cyan", f"{data_triees[cle_partie2]}\n"))
                                else:
                                    print(couleur_affichage("rouge", "La partie entre ces deux joueurs n'existe pas."))
                        
                case 2:
                    
                    souhait = erreur_entree_str(["o", "oui", "non", "n"], couleur_affichage("magenta", "🚪 Souhaitez-vous quitter ? (oui/o, non/n) : "),couleur_affichage("rouge", "❌ Entrée invalide."))
                
                    if souhait in ["o", "oui"]:
                        print(couleur_affichage("jaune", "Vous avez quitter le sous menu !"))
                        quitter = False

                case _:
                    print(couleur_affichage("rouge", "❌ Choix invalide !!!"))
                    

        

    except ValueError:
        print(couleur_affichage("rouge","Aucun fichier disponible"))
        print(couleur_affichage("rouge","Veuillez en crÃ©er un en lancant une partie \n"))


def erreur_entree_str(choix_valides: list[str], message: str, message_erreur: str) -> str:
    """
    Vérifie que l'entrée utilisateur est une chaîne valide.
    Si la liste `choix_valides` est vide, aucune restriction sur l'entrée.

    strip() enlève les espaces :
    texte = "   Bonjour !   "
    print(texte.strip())  # Résultat : "Bonjour !"

    Paramètres :

        - choix_valides: Liste des valeurs acceptées (vide signifie pas de restrictions).
        - message: Message pour utilisateur.
        - message_erreur: Message affiché si l'entrée est invalide.

    Retourne :

        - str: La chaîne saisie et validée.

    """
    
    while True:

        texte = input(message)

        # Vérifie si l'entrée est dans la liste des choix valides
        if not choix_valides or texte in choix_valides:
            return texte
        
        # Si l'entrée est invalide, afficher un message d'erreur
        print(message_erreur)


def erreur_entree_invalide_str(choix_invalides: list[str], message: str, message_erreur: str) -> str:
    """
    Vérifie que l'entrée utilisateur est une chaîne valide.
    Si la liste choix_valides est vide, aucune restriction sur l'entrée.

    strip() enlève les espaces :
    texte = "   Bonjour !   "
    print(texte.strip())  # Résultat : "Bonjour !"

    Paramètres :

        - choix_valides: Liste des valeurs acceptées (vide signifie pas de restrictions).
        - message: Message pour utilisateur.
        - message_erreur: Message affiché si l'entrée est invalide.

    Retourne :

        - str: La chaîne saisie et validée.
        
    """

    while True:

        texte = input(message)

        # Vérifie si l'entrée est dans la liste des choix valides
        if texte and texte not in choix_invalides:
            if "robot" not in texte:
                return texte 

        #Si l'entrée est invalide, afficher un message d'erreur
        print(message_erreur)


def erreur_entree(min: int, max: int, message: str, message_erreur: str, message_depassement: str) -> int :
    """
    Si les valeur de min et max sont à 0 les deux cela signifie qu'il n'y a pas de limite
    demandé par l'utilisateur

    Paramètre :

        - min : int
        - max : int
        - message : str
        - message_erreur : str
        - message_depassement : str

    Retourne : 
        
        - int : retourne la valeur qui respecte les paramètres
        
    """

    nombre : str | int
    while True:
        try:
            nombre = input(message)

            if not nombre:
                raise ValueError(message_erreur)

            nombre = conversion_chiffrelettre(nombre,message)

            # Si min et max sont tous les deux à 0, aucune limite n'est imposée
            if min == 0 and max == 0:
                return nombre

            #Sinon vérifie les limites min,max compris
            elif nombre < min or nombre > max:
                print(message_depassement)

            else :
                return nombre

        except ValueError:
            print(message_erreur)


def test_niveau(niveau : int) -> str:
    """ 
    Retourne le niveau en chaîne de caractère en fonction du niveau

    Paramètre :

        - niveau : int

    Retourne :

        - une chaîne de caractères
    
    """

    if niveau == 1:
        return "Facile"
    elif niveau == 2:
        return "Moyen"
    else:
        return "Difficle"


def adaptation(choix :int) -> tuple[str,str,int]:
    """
    Cette fonction permet de mettre les noms et le niveau 
    demandé pour les robots en paramètres de la fonction menu

    Paramètre :

        - choix (int) : Le choix détermine comment l'utilisateur va jouer (joueur contre joueur, robot contre robot...)

    Retourne : 

        - tuple[str,str,int] : Retourne les noms des deux joueurs et le niveau du robot pour les jeux

    """


    niveau : int
    joueur1 :str
    joueur2 : str

    if choix == 1:
        joueur1 = erreur_entree_invalide_str(choix_invalides=["", " "],message=couleur_affichage("cyan","Joueur 1: veuillez choisir votre pseudo : "),message_erreur = couleur_affichage("rouge","Le pseudo ne doit pas être vide, contenir uniquement des espaces, contenir 'robot' dans son pseudo ou être invalide.")).strip()
        joueur2 = erreur_entree_invalide_str(choix_invalides=["", " ", joueur1],message=couleur_affichage("jaune","Joueur 2: veuillez choisir votre pseudo : "),message_erreur=couleur_affichage("rouge","Le pseudo ne doit pas être vide, contenir uniquement des espaces, contenir 'robot' dans son pseudo ou être identique à celui du Joueur 1.")).strip()
        niveau = 0
            
    elif choix == 2:
        joueur1 = erreur_entree_invalide_str(choix_invalides=["", " "],message=couleur_affichage("cyan","Joueur 1: veuillez choisir votre pseudo : "),message_erreur = couleur_affichage("rouge","Le pseudo ne doit pas être vide, contenir uniquement des espaces, contenir 'robot' dans son pseudo ou être invalide.")).strip()
        niveau = proposition_difficulte()
        joueur2 = "Robot_" + test_niveau(niveau)

        print("")
        print(couleur_affichage("cyan",f"{joueur1} vous allez donc joueur contre {joueur2}"))

    else: 
        print(couleur_affichage("cyan","Choississer la difficulté des Robots : "))
        niveau = proposition_difficulte()
        joueur1 = "Robot1_" + test_niveau(niveau)
        joueur2 = "Robot2_" + test_niveau(niveau)

    return joueur1,joueur2,niveau



def testfichiers() -> bool:
    """
    Cette fonction sert simplement à vérifier que les fichiers JeuMorpion.py, JeuAllumettes.py et JeuDevinette.py soient bien dans le même dossier que menu.py

    Paramètres : 

        - Rien

    Retourne :

        - bool
    """

    fichierimport : list[str]

    fichierimport = ["JeuMorpion","JeuAllumettes","JeuDevinette"]

    for fichier in fichierimport:
        try :
            importlib.import_module(fichier)
        except ModuleNotFoundError:
            return False
    

    return True




if __name__ == "__main__":

    choix : int
    parametre : tuple[str,str,int]


    if testfichiers() == False:
        print(couleur_affichage("rouge","Vérifier que tous vos fichiers soient présents dans le dossier avant de lancer le programme !"))
    else:
        ################################################################
        """Import des fonctions pythons qui servent de jeux"""
        from JeuDevinette import devinette #import du jeu de la devinette
        from JeuAllumettes import allumettes #import du jeu des allumettes
        from JeuMorpion import morpion #import du jeu du morpion
        ################################################################
        """Lancement du menu"""
        choix = proposition_robot_joueur()
        parametre = adaptation(choix)
        menu(parametre[0],parametre[1],parametre[2],choix)