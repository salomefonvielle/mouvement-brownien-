# Mouvement_Brownien_by_group_19
 

# Nom :

Simulation Physique du mouvement Brownien 

# Description

Projet de deuxième semaine des Coding Weeks de CentraleSupelec P2026!
Nous allons le consacrer à la modélisation/simulation du mouvement Brownien.

# Equipe 


- Salomé Fonvielle (Déleguée du groupe) : 20 ans, j'aime la physique ( et la philo !) 
- Guillaume Dubois : J'aime la physique et l'escrime 
- Vianney Parent: Etudiant à Cs, j'aime beaucoup la physique et la montagne !
- Solène Duquenne : 19ans, vive le piano
- Lucie Broutin: je fais de l'escrime et joue du violon
- Hadrien Henriot: 20 ans, vive les fusées !

# Définition du MVP 
Représentation du mouvement Brownnien et des paramètres qui l'influencent 

# User story

En tant qu’utilisateur, je veux pouvoir paramétrer la simulation en termes de température, de nombre de particules dans l'enceinte et de taille des particules.

En tant qu’utilisateur, je veux pouvoir visualiser la particule suivie et la trajectoire que celle-ci décrit.


# Organisation du projet 

**Objectif 1 :** Marche aléatoire d'une particule

    ->Jalon1: Déplacement aléatoire d'un particule dans 4 directions
    ->Jalon2: Déplacement aléatoire d'une particule dans toutes les directions

**Objectif 2 :** Création d'un nuage de particules

    ->Jalon1: Représentation fixe du nuage 
    ->Jalon2: Mise en mouvement du nuage (aléatoire pour la direction et la position initiale)
    ->Jalon3: Rebonds sur les bords du cadre 

**Objectif 3 :** Collisions entre toutes les particules et particule suivie

    ->Jalon1: Mise en place de collisions entre toutes les particules
    ->Jalon2: Suivi d'une particule particulière
    ->Jalon3: Ajout de la trajectoire de la particule suivie

**Objectif 4 :** Création d'une interface graphique pour la simulation

    ->Jalon1: Création d'une maquette pour l'interface graphique
    ->Jalon2: Implémentation simple de l'interface
    ->Jalon3: Permettre le paramétrage de l'interface (sliders,boutons)

**Objectif 5 :** Amélioration, autre interface graphique, vérification de lois physiques (Bonus)

    ->Jalon1: Mouvement brownien avec pymunk
    ->Jalon2: Vérification de lois physiques par le modèle et mise en cohérence des grandeurs physiques
    ->Jalon3: Qualité de l'interface graphique et options supplémentaires
    ->Jalon4: tentative en 3D
