# Gaz Parfait & Mouvement Brownien

## Description du Projet

Ce projet, réalisé dans le cadre des **Coding Weeks de CentraleSupélec (P2026)**, consiste en le développement d'un moteur de simulation physique bidimensionnel modélisant un gaz parfait composé de particules en collisions élastiques.

L'objectif principal est de simuler le **Mouvement Brownien** et de valider numériquement les lois fondamentales de la thermodynamique à partir d'une approche multi-agents.

### Points Forts Techniques & Scientifiques

- **Moteur Physique Micro-Macro** : Implémentation d'un modèle de sphères dures avec gestion des collisions élastiques. Le moteur garantit la conservation de la quantité de mouvement et de l'énergie cinétique.
- **Validation Thermodynamique** :
    - Vérification empirique de la **Loi des Gaz Parfaits** ($PV = nRT$) via une régression linéaire pression-température.
    - Observation de la convergence vers la **distribution des vitesses de Maxwell-Boltzmann**.
- **Interface Interactive** : Développement d'une GUI (Tkinter + Matplotlib) permettant le pilotage dynamique de la simulation (température, densité, rayon des particules, suivi de trajectoire).
- **Architecture Logicielle** : Structure modulaire, gestion des dépendances et validation par tests unitaires automatisés.

---

## Fonctionnalités (MVP)

- **Paramétrage dynamique** : Température, nombre de particules, taille.
- **Visualisation interactive** : Animation en temps réel des particules dans une enceinte carrée.
- **Suivi de particule** : Tracé en temps réel de la trajectoire d'une particule spécifique pour illustrer le mouvement brownien.
- **Analyses Graphiques** : Distribution des vitesses et vérification de la loi des gaz parfaits.

---

## Structure du Projet

```
src/
├── physics/                # Moteur de simulation (physique & calculs)
│   ├── definitions_objets.py
│   └── fonctions_auxiliaires.py
├── visualization/          # Animation et interface graphique
│   ├── animation_particules.py
│   ├── animation_graphique.py
│   └── gazparfaits_graphique.py
└── main.py                 # Point d'entrée de l'application (Tkinter)

tests/                      # Tests unitaires (Pytest)
docs/                       # Présentation et documentation
experiments/                # Prototypes (Marche aléatoire, Pymunk)
```

---

## Installation & Utilisation

### Installation

1. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Linux/macOS
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

### Lancement

Pour démarrer l'interface interactive :
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python src/main.py
```

### Tests

Pour exécuter les tests unitaires :
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest tests/
```

---

## Équipe (Groupe 4 - Coding Weeks)

- Guillaume Dubois
- Vianney Parent
- Solène Duquenne
- Lucie Broutin
- Hadrien Henriot
- Salomé Fonvielle
