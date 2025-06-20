# random donne un nombre aléatoire dans un intervalle
from random import randint

def afficher_allumettes(nbr_allumettes: int) -> None:
    from Menu import couleur_affichage
    """
    Affiche sur la console les allumettes restantes.

    Paramètre:

    - nbr_allumettes (int): Le nombre d'allumettes restant à afficher.

    Retourne:

        Elle ne retourne rien

    """
    print("\n" + couleur_affichage("bleu", "🪄 " * nbr_allumettes))
    print(couleur_affichage("cyan", f"Il reste : {nbr_allumettes} allumettes.\n"))


def niv1() -> int:
    """
    Cette fonction crée le robot niveau 1

    Retourne:

        - int : retourne le nombre d'allumettes que le robot à pris

    """
    return randint(1,3)


def niv2(nbr_allumettes: int) -> int:
    """
    Cette fonction crée le robot niveau 2

    Paramètre:

        - nbr_allumettes (int): Le nombre d'allumettes restant à afficher
    
    Retourne:

        - int : retourne le nombre d'allumettes que le robot à pris
        
    """
    if nbr_allumettes > 4 :
        return randint(1,3)  

    else: 
        
        if nbr_allumettes == 1 :
            return 1
        else :
            return nbr_allumettes - 1


def niv3(nbr_allumettes : int) -> int:
    """
    Cette fonction crée le robot niveau 3

    Paramètre:

        - nbr_allumettes (int): Le nombre d'allumettes restant à afficher
    
    Retourne:

        - int : retourne le nombre d'allumettes que le robot à pris
        
    """
    recup : int
    
    recup = 1
    if nbr_allumettes > 4:

        #Verifie si c'est un multiple de 4
        while (nbr_allumettes - recup) % 4 != 1 and recup <= 2:
            recup += 1        

    else:

            if nbr_allumettes <= 4 and nbr_allumettes != 1:
                recup = nbr_allumettes - 1
    
    return recup


def robot(nbr_allumettes : int, niveau : int,joueur1 : str, joueur2 : str,quiJoue : int) -> int:
    """
    Fonction qui execute en fonction du niveau le robot en lui donnant
    le nombre d'allumettes

    Paramètre:

        - nbr_allumettes (int): Le nombre d'allumettes restant à afficher
        - niveau (int): Variable qui prend le niveau du robot demandé
        - joueur1 (str): Le nom du joueur 1
        - joueur2 (str): Le nom du joueur 2
        - quiJoue (int): Le joueur qui joue actuelement
    
    Retourne:

        - int: Renvoie la nombre d'allumettes que le robot a choisit

    """
    from Menu import couleur_affichage
    import time

    recup : int 

    if niveau == 1 :
        recup = niv1()
    elif niveau == 2:
        recup = niv2(nbr_allumettes)
    else:
        recup = niv3(nbr_allumettes)

    print(couleur_affichage("jaune",f"Le {joueur1 if quiJoue ==1 else joueur2} réfléchi ..."))
    time.sleep(1.5)
    print(couleur_affichage("jaune",f"Le {joueur1 if quiJoue == 1 else joueur2} a pris {recup} allumette(s)"))
    return recup


def allumettes(joueur1 :str,joueur2 : str , niveau : int, tours : int,quiJoue : int) -> str:
    """
    Jeu allumettes :

    Tant que aucun joueurs n'a atteint le nombre de tours nécessaire pour gagner,
    les joueurs continue de jouer. Si un des joueurs s'appellent "bot" alors un robot va jouer

    Paramètre :

        - Joueur(str) : Prend le nom du joueur 1
        - Joueur(str) : Prend le nom du joueur 2
        - niveau(int) : Le niveau du robot
        - tours(int) : Le nombre de tours a joué pour gagné
        - quiJoue(int) : Le joueur qui va jouer

    Retourne :

        - str : Envoie le nom du joueur

    """
    from Menu import couleur_affichage, erreur_entree, changer_joueur,contient_robot

    resultatjoueur1 : int
    resultatjoueur2 : int
    nbr_allumettes : int
    recup : int

    resultatjoueur1 = 0
    resultatjoueur2 = 0 
    recup = 0

    while resultatjoueur1 != tours and resultatjoueur2 != tours:
        # Début d'une nouvelle manche avec 20 allumettes

            print(couleur_affichage("cyan", "💡 Début d'une nouvelle manche !"))

            nbr_allumettes = 20

            while nbr_allumettes > 0:

                # Affiche le nombre des allumettes restantes
                afficher_allumettes(nbr_allumettes)

                if quiJoue == 1 :
                    if contient_robot(joueur1) == False :
                        recup = erreur_entree(1, 3,couleur_affichage("vert", f"{joueur1} : Combien d'allumettes voulez-vous prendre ? "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre !"),couleur_affichage("rouge", "⚠️ Nombre hors limites ! Veuillez entrer un nombre entre 1 et 3."))
                    
                    else :
                        recup = robot(nbr_allumettes,niveau,joueur1,joueur2,quiJoue)
                
                else :
                    if contient_robot(joueur2) == False:
                        recup = erreur_entree(1, 3,couleur_affichage("magenta", f"{joueur2} : Combien d'allumettes voulez-vous prendre ? "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre !"),couleur_affichage("rouge", "⚠️ Nombre hors limites ! Veuillez entrer un nombre entre 1 et 3."))
                    
                    else :
                        recup = robot(nbr_allumettes,niveau,joueur1,joueur2,quiJoue)


                # Vérifie si le joueur peut prendre tant d'allumettes
                while nbr_allumettes - recup < 0:
                    print(couleur_affichage("rouge", "⚠️  Pas assez d'allumettes disponibles !"))
                    afficher_allumettes(nbr_allumettes)
                    
                    if quiJoue == 1:
                        if contient_robot(joueur1) == False:
                            recup = erreur_entree(1, 3,couleur_affichage("vert", f"{joueur1} : Combien d'allumettes voulez-vous prendre ? "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre !"),couleur_affichage("rouge", "⚠️ Nombre hors limites ! Veuillez entrer un nombre entre 1 et 3."))
                        else:
                            recup = robot(nbr_allumettes,niveau,joueur1,joueur2,quiJoue)
                   
                    else:
                        if contient_robot(joueur2) == False:
                            recup = erreur_entree(1, 3,couleur_affichage("magenta", f"{joueur2} : Combien d'allumettes voulez-vous prendre ? "),couleur_affichage("rouge", "❌ Entrée invalide. Veuillez entrer un nombre !"),couleur_affichage("rouge", "⚠️ Nombre hors limites ! Veuillez entrer un nombre entre 1 et 3."))
                        else:
                            recup = robot(nbr_allumettes,niveau,joueur1,joueur2,quiJoue)

                nbr_allumettes -= recup

                # Passe au joueur suivant
                quiJoue = changer_joueur(quiJoue)

            # Affiche l'état final des allumettes
            afficher_allumettes(nbr_allumettes)

            # Mise à jour du score du joueur ayant remporté la manche
            if quiJoue == 1:
                resultatjoueur1 += 1
                print(couleur_affichage("vert", f"🏆 {joueur1} a remporté cette manche !"))

            else:
                resultatjoueur2 += 1
                print(couleur_affichage("magenta", f"🏆 {joueur2} a remporté cette manche !"))

            # Affiche les scores après chaque manche
            print(couleur_affichage("cyan", f"📊 Score actuel - {joueur1}: {resultatjoueur1} | {joueur2}: {resultatjoueur2}\n"))

            # Passe au joueur suivant pour commencer la nouvelle manche
            quiJoue = changer_joueur(quiJoue)

    # Affiche le gagnant
    if resultatjoueur1 == tours:
        print(couleur_affichage("vert", f"🎉 {joueur1} a gagné la partie ! Félicitations !"))
        return joueur1
    else:
        print(couleur_affichage("magenta", f"🎉 {joueur2} a gagné la partie ! Félicitations !"))
        return joueur2