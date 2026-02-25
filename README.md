# Mouvement_Brownien_by_group_19

# Simulation Physique du Mouvement Brownien

Projet réalisé lors de la deuxième semaine des Coding Weeks de CentraleSupélec (P2026).

Ce projet est consacré à la modélisation et à la simulation numérique du mouvement brownien, à travers une représentation d’un gaz parfait bidimensionnel composé de particules en collision élastique.

---

## Équipe


- **Guillaume Dubois**
- **Vianney Parent**
- **Solène Duquenne**
- **Lucie Broutin**
- **Hadrien Henriot**
- **Salomé Fonvielle** 

---

## Définition du MVP

Représentation du mouvement brownien et des paramètres qui l’influencent :

- Température
- Nombre de particules
- Taille des particules
- Visualisation de la trajectoire d’une particule suivie

---

## User Stories

- En tant qu’utilisateur, je veux pouvoir paramétrer la simulation (température, nombre de particules, taille).
- En tant qu’utilisateur, je veux visualiser la particule suivie et sa trajectoire.

---

## Organisation du Projet (Développement Progressif)

### Objectif 1 : Marche aléatoire d’une particule

- Jalon 1 : Déplacement aléatoire dans 4 directions
- Jalon 2 : Déplacement aléatoire dans toutes les directions

### Objectif 2 : Création d’un nuage de particules

- Jalon 1 : Représentation fixe
- Jalon 2 : Mise en mouvement aléatoire
- Jalon 3 : Rebonds sur les bords

### Objectif 3 : Collisions entre particules

- Jalon 1 : Collisions entre toutes les particules
- Jalon 2 : Suivi d’une particule particulière
- Jalon 3 : Ajout de la trajectoire de la particule suivie

### Objectif 4 : Interface graphique

- Jalon 1 : Maquette
- Jalon 2 : Implémentation simple
- Jalon 3 : Paramétrage dynamique (sliders, boutons)

### Objectif 5 : Améliorations (Bonus)

- Mouvement brownien avec Pymunk
- Vérification des lois physiques
- Amélioration de l’interface
- Tentative en 3D

---

# Modèle Scientifique

Ce projet modélise un gaz parfait bidimensionnel constitué de particules rigides dans une enceinte carrée unité :

- Collisions élastiques particule–particule
- Collisions élastiques particule–paroi
- Conservation de la quantité de mouvement
- Conservation de l’énergie cinétique
- Observation empirique de la distribution de Maxwell–Boltzmann
- Vérification numérique de la loi des gaz parfaits

# Structure du Projet

```
docs/                       # Présentation du projet
experiments/                # Prototypes indépendants
    ├── Marche_aleatoire/
    └── Pymunk/

src/
│
├── physics/                # Moteur de simulation
│   ├── definitions_objets.py
│   └── fonctions_auxiliaires.py
│
├── visualization/          # Animation et interface graphique
│   ├── animation_particules.py
│   ├── animation_graphique.py
│   ├── gazparfaits_graphique.py
│  
│
└── __init__.py


tests/                      # Tests unitaires

```
interface.py   # Lancement de la simulation  
---

# Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Ou installer en mode editable :

```bash
pip install -e .
```

---

# Lancer la Simulation

```bash
python -m interface
```

L’interface permet :

- Choix du nombre de particules
- Réglage du rayon
- Paramétrage de la température
- Suivi d’une particule
- Visualisation de la distribution des vitesses
- Vérification numérique de la loi des gaz parfaits

---

# Tests

```bash
pytest
```

Couverture :

```bash
coverage run -m pytest
coverage html
```

---

## Validation Thermodynamique

Une régression linéaire pression-température permet d’estimer la constante des gaz parfaits.

---

# Documentation

Présentation complète disponible dans :

```
docs/Presentation_CW.pdf

```
