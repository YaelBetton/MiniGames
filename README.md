# 🤖 SAE S1.02 – Mini-Jeux avec des robots

## 👥 Auteurs
- **Rémi Bastide** 
- **Yaël Betton**

## 🎯 Objectif du Projet

L'objectif de cette SAE est d'améliorer notre travail précédent (SAE S1.01) en ajoutant :
- Des **robots (IA)** avec plusieurs **niveaux de difficulté** (facile, moyen, imbattable),
- Des **modes de jeu** (joueur contre joueur, joueur contre robot, robot contre robot),
- Une **meilleure organisation du code** et une **optimisation générale**.

Trois jeux classiques ont été enrichis d'une intelligence artificielle :
1. **Devinette**
2. **Jeu des Allumettes**
3. **Morpion (Tic-Tac-Toe)**

---

## 🎮 Présentation des Mini-Jeux

### 🔢 Devinette

- **Principe** : Trouver un nombre mystère entre 0 et 100.
- **IA** :
  - **Niveau 1** : Propose aléatoirement un nombre dans les bornes.
  - **Niveau 2** : Utilise une **dichotomie** (milieu des bornes).
  - **Niveau 3** : Même que le niveau 2, mais avec **7 tentatives optimales** → imbattable.

### 🕯️ Allumettes

- **Principe** : Retirer 1 à 3 allumettes, éviter de prendre la dernière.
- **IA** :
  - **Niveau 1** : Choix aléatoire.
  - **Niveau 2** : Joue intelligemment en fin de partie.
  - **Niveau 3** : Tente de toujours laisser `4n - 1` allumettes à l'adversaire → stratégie optimale.

### ❌ Morpion

- **Principe** : Aligner 3 symboles.
- **IA** :
  - **Niveau 1** : Joue aléatoirement.
  - **Niveau 2** : Cherche à gagner s’il le peut, sinon joue aléatoirement.
  - **Niveau 3** : Utilise **Minimax** avec profondeur, **imbattable**.

---

## 🧠 Fonctionnalités Avancées

### 🧩 Menu Principal

Ajout d'un menu interactif permettant :
- De choisir les **noms et modes de jeu** (joueur/joueur, joueur/robot, robot/robot),
- De sélectionner le **niveau de difficulté des robots**,
- D'accéder aux **règles** et à une **explication des scores**.

### 📊 Gestion des Scores

- Sauvegarde dans un fichier **JSON** pour une meilleure lisibilité.
- Système de points évolutif selon la difficulté du robot.
- Interface d’affichage des scores avec tri, recherche et filtres.

### 🧪 Tests

Des tests ont été effectués sur tous les jeux pour :
- Valider les comportements des IA selon les niveaux,
- Vérifier les cas de victoire/défaite/égalité,
- Garantir la stabilité de l’ensemble du programme.

---

## 🛠️ Technologies & Librairies

- **Python 3**
- Utilisation de :
  - `random` pour les choix aléatoires,
  - `importlib` pour l’import dynamique de modules,
  - `json` pour la gestion des scores.

---

## 📁 Organisation du Projet

```bash
📦 Projet_SAE_S1.02
 ┣ 📄 JeuDevinette.py
 ┣ 📄 JeuAllumettes.py
 ┣  📄 JeuMorpion.py
 ┣ 📄 menu.py
 ┗ 📄 Compte_rendu_S1.02.pdf
