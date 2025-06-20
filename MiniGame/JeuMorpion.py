# Liste des combinaisons gagnantes du jeu, chaque sous-liste représente une ligne.
coupsGagnants : list[list[int]]
coupsGagnants = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# Liste des cases jouées par le joueur 1.
joueur1Coups : list[int]
joueur1Coups = []

# Liste des cases jouées par le joueur 2.
joueur2Coups : list[int]
joueur2Coups = []

# Représentation initiale du plateau de jeu , si case = 0 (vide).
plateau : list[list[int]]
plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



def symbole(case: int, position: int) -> str:
    from Menu import couleur_affichage
    """
    Convertie une case du plateau en symbole de jeu.

    Paramètre:

        case (int): Entier représentant la case (0 = vide, 1 = X pour le joueur 1, 2 = O pour le joueur 2).
        position (int): Position de la case pour l'affichage si elle est vide.

    Retourne:

        str: Symbole affiché pour la case ('-' = vide, 'X' = joueur 1, 'O' = joueur 2).

    """
    if case == 1:
        return couleur_affichage("rouge", "X")
    
    elif case == 2:
        return couleur_affichage("bleu", "O")
    
    else: 
        return str(position)


def attribution_choix(plateau: list[list[int]], quiJoue: int, CaseJoue: list[list[int]]) -> None:
    """
    Met à jour le plateau en attribuant le choix du joueur à une case.

    Paramètre:

        - plateau (list[list[int]]): Représentation du plateau sous forme de liste de listes.
        - quiJoue (int): Numéro du joueur actuel (1 ou 2).
        - CaseJoue (list[list[int]]): Liste des coups en fonction de chaque joueur

    """
    ligne : int
    colonne : int 
    symbole_joueur : int
    dernierCoup : int

    if quiJoue == 1:
        dernierCoup = CaseJoue[0][-1]
        symbole_joueur = 1
    else:
        dernierCoup = CaseJoue[1][-1]
        symbole_joueur = 2
    
    # Placement sur le plateau grâce au numéro de la case
    ligne = (dernierCoup - 1) // 3  # Détermine la ligne
    colonne = (dernierCoup - 1) % 3  # Détermine la colonne

    # Mise à jour de la case du plateau
    plateau[ligne][colonne] = symbole_joueur


def afficher_plateau(plateau: list[list[int]]) -> None:

    from Menu import couleur_affichage

    """

    Affiche le plateau actuel en convertissant les cases en symboles.

    Paramètre:

        - plateau (list[list[int]]): La représentation actuelle du plateau de jeu sous forme de liste de listes.

    """
    position : int
    largeur : int

    position = 1  # Initialise la position de départ
    
    # Affiche chaque ligne du plateau avec ses symboles
    for largeur in range(3):
        print(symbole(plateau[largeur][0], position), "|", symbole(plateau[largeur][1], position + 1), "|", symbole(plateau[largeur][2], position + 2))

        if largeur < 2:
            # Séparation entre les lignes
            print(couleur_affichage("jaune", "--+---+--"))

        position += 3


def verif_gagnant(CaseJoue: list[list[int]],quiJoue : int) -> int:
    """

    Vérifie si l'un des joueurs a une combinaison gagnante.

    Paramètre:

        - CaseJoue (list[list[int]]): Liste des coups joués pour chaque joueur.
        - quiJoue (int) : Le joueur qui joue actuellement

    Retourne:

        int : Si renvoie 0 : pas encore de gagnant, si renvoie 1 : Gagnant , si renvoie 2 : Egalite

    """
    combinaison : list[int]
    coup : int
    compteur_joueur1 : int
    compteur_joueur2 : int

    for combinaison in coupsGagnants:
        # Réinitialise les compteurs pour éviter d'avoir un "faux" gagnant
        compteur_joueur1 = 0
        compteur_joueur2 = 0

        # Balayage de balayage car les listes sont ordonnées et donc il faut vérifier qu'on n'est pas les bons nombres dans le désordre
        for coup in combinaison:
            if coup in CaseJoue[0]:
                compteur_joueur1 += 1
            if coup in CaseJoue[1]:
                compteur_joueur2 += 1

        # Si l'un des compteur atteint 3 il y aura un gagnant
        if compteur_joueur1 == 3:
            return 1
        if compteur_joueur2 == 3:
            return 1

        if compteur_joueur1 == 2 and quiJoue == 1:
            # Cherche case manquante pour trouver la combinaison
            for coup in combinaison:
                if coup not in CaseJoue[0] and coup not in CaseJoue[1]:
                    return coup + 10

        # Si joueur 2 proche de gagner il cherche la case qui manque pour gagner
        if compteur_joueur2 == 2 and quiJoue == 2:
            for coup in combinaison:
                if coup not in CaseJoue[0] and coup not in CaseJoue[1]:
                    return coup + 10
        
        # Si toutes les cases sont occupées et aucune combinaison gagnante, c'est une égalité
    if len(CaseJoue[0]) + len(CaseJoue[1]) == 9 :
        return 2
    
    return 0


def verif_gagnant_ordi(CaseJoue: list[list[int]]) -> int:
    """

    Vérifie si l'un des joueurs a une combinaison gagnante.

    Paramètre:

        CaseJoue (list[list[int]]): Liste des coups joués pour chaque joueur.

    Retourne:

        int : Si renvoie -3 : égalité, si renvoie -1 : Joueur1 gagne , si renvoie -2 : Joueur 2 gagne, si renvoie -4 aucun gagne
        sinon renvoie la case sur laquelle on peut gagber

    """
    combinaison : list[int]
    coup : int
    compteur_joueur1 : int
    compteur_joueur2 : int

    for combinaison in coupsGagnants:
        # Réinitialise les compteurs pour éviter d'avoir un "faux" gagnant
        compteur_joueur1 = 0
        compteur_joueur2 = 0

        # Balayage de balayage car les listes sont ordonnées et donc il faut vérifier qu'on n'est pas les bons nombres dans le désordre
        for coup in combinaison:
            if coup in CaseJoue[0]:
                compteur_joueur1 += 1
            if coup in CaseJoue[1]:
                compteur_joueur2 += 1

        # Si l'un des compteur atteint 3 il y aura un gagnant
        if compteur_joueur1 == 3:
            return 1
        if compteur_joueur2 == 3:
            return 2
    
    return 4


def reinitialiser_partie(plateau: list[list[int]], CaseJoue: list[list[int]]) -> None:
    """
    Réinitialise le plateau et les listes des cases jouées.

    Paramètre:

        plateau (list[list[int]]): Le plateau de jeu à réinitialiser.
        CaseJoue (list[list[int]]): Liste des cases jouées par les joueurs.

    """
    largeur : int
    hauteur : int

    for largeur in range(3):
        for hauteur in range(3):
            plateau[largeur][hauteur] = 0  # Réinitialise les cases du plateau
    CaseJoue[0].clear()  # Vide la liste des coups du joueur 1
    CaseJoue[1].clear()  # Vide la liste des coups du joueur 2


def quiJoueCoups(quiJoue: int, CaseJoue: list[list[int]], joueur1: str, joueur2: str, niveau : int) -> list[list[int]]:

    from Menu import erreur_entree,couleur_affichage,contient_robot
    import time

    """

    Demande au joueur actuel de sélectionner une case pour jouer, vérifie si le coup est dans le plateau sinon redemande de jouer le coup.

    Paramètre:

        quiJoue (int): Numéro du joueur actuel (1 ou 2).
        CaseJoue (list[list[int]]): Liste des cases jouées par chaque joueur.
        joueur1 (str): Nom du joueur 1.
        joueur2 (str): Nom du joueur 2.
        niveau (int): Le niveau des robots

    Retourne:

        list[list[int]]: Mise à jour des coups joués par les deux joueurs.

    """
    message : str
    dernierCoup : int

    message = couleur_affichage("bleu", f"{joueur1} : Sur quelle case voulez-vous jouer : ") if quiJoue == 1 else couleur_affichage("magenta", f"{joueur2} : Sur quelle case voulez-vous jouer : ")
    
    if contient_robot(joueur1) == False and quiJoue == 1:
        # Affiche le texte en couleur + Demande la case sur laquelle le joueur veut jouer et enfin vérifie si cette case et compris entre 1 et 9
        dernierCoup = erreur_entree(1, 9, message, couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"), couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 9."))
        # Vérifie que la case est libre
        while dernierCoup in CaseJoue[0] or dernierCoup in CaseJoue[1]:
            print(couleur_affichage("rouge", "⚠️  Case déjà jouée, veuillez resaisir une autre case !"))
            dernierCoup = erreur_entree(1, 9, message, couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"), couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 9."))
    
    elif contient_robot(joueur2) == False and quiJoue == 2:
        # Affiche le texte en couleur + Demande la case sur laquelle le joueur veut jouer et enfin vérifie si cette case et compris entre 1 et 9
        dernierCoup = erreur_entree(1, 9, message, couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"), couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 9."))
        # Vérifie que la case est libre
        while dernierCoup in CaseJoue[0] or dernierCoup in CaseJoue[1]:
            print(couleur_affichage("rouge", "⚠️  Case déjà jouée, veuillez resaisir une autre case !"))
            dernierCoup = erreur_entree(1, 9, message, couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre entier !"), couleur_affichage("rouge", "⚠️  Nombre hors limites ! Veuillez entrer un nombre entre 1 et 9."))

    else: 
        print(couleur_affichage("jaune",f"Le {joueur1 if quiJoue ==1 else joueur2} réfléchi ..."))
        time.sleep(1.5)
        if niveau == 1:
            dernierCoup = niv1(CaseJoue)
        
        elif niveau == 2:
            dernierCoup = niv2(CaseJoue,quiJoue)

        else : 
            dernierCoup = niv3(CaseJoue,quiJoue)
    

    # Enregistre le coup du joueur
    if quiJoue == 1:
        CaseJoue[0].append(dernierCoup)
    else:
        CaseJoue[1].append(dernierCoup)

    return CaseJoue


def coup_ordi(plateau: list[list[int]], quiJoue: int, CaseJoue: list[list[int]]) -> int:
    """
    Fonction qui détermine le meilleur coup du robot niveau 3 en utilisant l'algorithme Minimax

    Paramètre :

        - plateau (list[list[int]]) : Le plateau de jeu avec les coups de chaques joueurs
        - quiJoue (int) : Le joueur qui joue actuellement
        - CaseJoue (list[list[int]]) : Liste des cases jouées par chaque joueur

    Retourne :

        - int : La meilleure case à jouer pour l'ordinateur

    """
    import random

    meilleur_score : int
    meilleurs_coups : list[int]
    largeur : int
    longueur : int
    case : int
    score : int
    meilleur_score : int


    meilleur_score = -1000
    # Liste qui enregistre les meilleurs possibilités
    meilleurs_coups = []

    for largeur in range(3):
        for longueur in range(3):

            if plateau[largeur][longueur] == 0:

                case = largeur * 3 + longueur + 1
                if quiJoue == 1:
                    CaseJoue[0].append(case)
                    plateau[largeur][longueur] = 1
                else:
                    CaseJoue[1].append(case)
                    plateau[largeur][longueur] = 2

                score = minimax(plateau, 0, False, quiJoue, CaseJoue,9)

                if quiJoue == 1:
                    CaseJoue[0].pop()
                else:
                    CaseJoue[1].pop()
                
                plateau[largeur][longueur] = 0


                if score > meilleur_score:
                    meilleur_score = score
                    meilleurs_coups = [case]
                elif score == meilleur_score:
                    meilleurs_coups.append(case)

    # Choisir un coup aléatoire parmi les meilleurs
    return random.choice(meilleurs_coups)


def minimax(plateau: list[list[int]], profondeur: int, maximiser: bool, quiJoue: int, CaseJoue: list[list[int]], profondeur_max: int) -> int:
    """
    Cette fonction est récursive et pour chaque coup il va attribuer 100 points si le robot peut gagner
    -100 si ce coup fait gagner l'adversaire et 0 s'il y a une égalité.

    La fonction minimax va chercher le meilleur coup si c'est le robot qui joue en prennant le meilleur score possible.

    Si c'est à l'adversaire de jouer il va chercher le plus petit score pour éviter qu'il gagne.

    Plus le coup pour gagner va être loin plus le score va être diminuer pour faire gagner le robot plus vite (max_profondeur = 9)

    Paramètre :

        - plateau (list[list[int]]) : Prend le plateau avec les coups joués par chaque joueur
        - profondeur (int) : Le nombre de coup pour atteindre un objectif (victoire,défaite,égalité)
        - maximiser (bool) : Permet de savoir si le joueur actuel doit maximiser ou minimiser le score
        - quiJoue (int) : Permet de savoir qui joue
        - CaseJoue (list[list[int]]) : Mémorise où chaque joueur a joué
        - profondeur_max (int) : Prend le nombre de calculs maximum que l'algorithme doit effectuer avant de s'arrêter

    Retourne : 

        - int : Retourne le meilleur coup possible pour le joueur actuel

    """
    from Menu import changer_joueur

    meilleur_score : int
    score : int
    largeur : int 
    longueur : int
    case : int
    adversaire : int

    
    # Condition de fin de recursivité
    if verif_gagnant_ordi(CaseJoue) == quiJoue:
        return 100 - profondeur

    elif verif_gagnant_ordi(CaseJoue) == changer_joueur(quiJoue):
        return -100 + profondeur

    elif len(CaseJoue[0]) + len(CaseJoue[1]) == 9:
        return 0

    elif profondeur >= profondeur_max:
        return 0


    if maximiser :

        meilleur_score = -1000

        for largeur in range(3):
            for longueur in range(3):

                if plateau[largeur][longueur] == 0:

                    case = largeur * 3 + longueur + 1
                    CaseJoue[0 if quiJoue == 1 else 1].append(case)
                    if quiJoue == 1 :
                        plateau[largeur][longueur] = 1
                    else : 
                        plateau[largeur][longueur] = 2

                    score = minimax(plateau, profondeur + 1, False, quiJoue, CaseJoue, profondeur_max)

                    CaseJoue[0 if quiJoue == 1 else 1].pop()
                    
                    plateau[largeur][longueur] = 0

                    # Mettre à jour le meilleur score
                    if score > meilleur_score : 
                        meilleur_score = score

        return meilleur_score

    else :

        meilleur_score = 1000
        adversaire = changer_joueur(quiJoue)

        for largeur in range(3):
            for longueur in range(3):

                if plateau[largeur][longueur] == 0:
                    # Test le coup et vérifie s'il est bien puis il est suprrimé

                    case = largeur * 3 + longueur + 1
                    CaseJoue[0 if adversaire == 1 else 1].append(case)
                    if adversaire == 1:
                        plateau[largeur][longueur] = 1
                    else : 
                        plateau[largeur][longueur] = 2

                    score = minimax(plateau, profondeur + 1, True, quiJoue, CaseJoue, profondeur_max)

                    CaseJoue[0 if adversaire == 1 else 1].pop()
                    plateau[largeur][longueur] = 0

                    if score < meilleur_score :
                        meilleur_score = score

        return meilleur_score



def niv1(CaseJoue : list[list[int]]) -> int:
    """
    Robot de niveau 1 joue aléatoirement

    Paramètre :
        
        - CaseJoue : Correspond au coup déjà joué

    Retourne :

        - int : Case joué par le robot

    """
    from random import randint

    dernierCoup : int

    dernierCoup = randint(1,9)
    while dernierCoup in CaseJoue[0] or dernierCoup in CaseJoue[1]:
        dernierCoup = randint(1,9)
    
    return dernierCoup


def niv2(CaseJoue : list[list[int]],quiJoue :int) -> int:
    """
    Si le robot peut jouer sur une case gagnate il le fait
    sinon il joue aléatoirement

    Paramètre :

        - CaseJoue : Les coups joue par les deux joueur
        - quiJoue : Joueur qui joue actuellement

    Retourne :

        - int : L'emplacement de la case choisi par le robot

    """
    case : int|None
    from random import randint

    # Vérifie si le robot peut gagner
    case = (verif_gagnant(CaseJoue,quiJoue) - 10)
    if case >= 0:
        return case

    # Sinon, joue aléatoirement
    case = randint(1, 9)
    while case in CaseJoue[0] or case in CaseJoue[1]:
        case = randint(1, 9)
    return case


def niv3(CaseJoue : list[list[int]],quiJoue : int) -> int:
    """
    Robot de niveau 3 jouant avec l'algorithme Minimax.

    Paramètre :

        - CaseJoue (list[list[int]]) : Les coups joué en fonction des joueurs
        - quiJoue (int) : Le joueur qui joue actuellement

    Retourne :

        - Le coup joué par le robot niveau 3

    """
    return coup_ordi(plateau,quiJoue,CaseJoue)


def morpion(joueur1 : str, joueur2 : str, niveau : int, tours : int, quiJoue : int) -> str:

    from Menu import couleur_affichage,changer_joueur,contient_robot
    """

    Gère le déroulement du jeu de morpion jusqu'à ce qu'il y ait un gagnant.

    Paramètre:

        quiJoue (int): Numéro du joueur qui commence.
        CaseJoue (list[list[int]]): Liste des cases jouées par chaque joueur.
        plateau (list[list[int]]): Plateau de jeu initialisé.

    Retourne : 

        str : Retourne le nom du joueur qui a gagné    
    
    """
    resultatjoueur1 : int # Compte le nombre de partie gagné par ce joueur
    resultatjoueur2 : int # Compte le nombre de partie gagné par ce joueur
    CaseJoue : list[list[int]]

    CaseJoue = [[],[]]
    resultatjoueur1 = 0
    resultatjoueur2 = 0

    print(" ")
    afficher_plateau(plateau)
    print(" ")

    # Boucle qui tant qu'un des deux joueurs n'a pas gagné continue de faire des parties
    while resultatjoueur1 != tours and resultatjoueur2 != tours:
        
        # Boucle tant que aucun joueur n'a gagné ou aucune égalité
        while verif_gagnant(CaseJoue, quiJoue) != 1 and verif_gagnant(CaseJoue,quiJoue) != 2:
            
            quiJoue = changer_joueur(quiJoue)

            if quiJoue == 1:
                print(couleur_affichage("bleu", f"{joueur1} doit jouer"))
            else :
                print(couleur_affichage("magenta", f"{joueur2} doit jouer"))

            CaseJoue = quiJoueCoups(quiJoue, CaseJoue, joueur1, joueur2,niveau)

            attribution_choix(plateau, quiJoue, CaseJoue)
            print(" ")
            afficher_plateau(plateau)
            print(" ")

        # Augmente les scores en fonction des parties gagnées
        if verif_gagnant(CaseJoue,quiJoue) == 1:
            if quiJoue == 1:
                resultatjoueur1 += 1
                print(" ")
                print(couleur_affichage("vert", f"🎉 {joueur1} a gagné 🎉"))
            else :
                resultatjoueur2 += 1
                print(" ")
                print(couleur_affichage("vert", f"🎉 {joueur2} a gagné 🎉"))
        
        elif verif_gagnant(CaseJoue,quiJoue) == 2 :
            print(couleur_affichage("magenta", "Égalité, aucun des deux joueurs n'a gagné."))
            if niveau == 3 and contient_robot(joueur1) and contient_robot(joueur2):
                tours -= 1

        reinitialiser_partie(plateau, CaseJoue)

        print(couleur_affichage("cyan", f"Voici le resultat de {joueur1} : {resultatjoueur1}"))
        print(couleur_affichage("cyan", f"Voici le resultat de {joueur2} : {resultatjoueur2}"))

        if resultatjoueur1 != tours and resultatjoueur2 != tours:
            print(couleur_affichage("magenta", "Partie suivante") + "\n")
            afficher_plateau(plateau)

    if not contient_robot(joueur1) or not contient_robot(joueur2) and niveau != 3:
        if quiJoue == 1:
            print(couleur_affichage("vert", f"🎉 {joueur1} a gagné cette partie! 🎉"))
            return joueur1
        else :
            print(couleur_affichage("vert", f"🎉 {joueur2} a gagné cette partie! 🎉"))
            return joueur2
    
    # Cas où on ne compte pas le score vu que c'est robot vs robot et que robot different 3
    return joueur1