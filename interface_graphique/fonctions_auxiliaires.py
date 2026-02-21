# Fonctions diverses pour gérer les trajectoires des particules ( chocs, ...)

# Importation des modules nécessaires
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
from interface_graphique.definitions_objets import *

# Fonction pour tracer une particule exceptionnelle (celle que l'on suit) en rouge


def Trace_particule_exception(p, ax):
    cpart = Circle((p.x, p.y), radius=p.r, color='red')
    ax.add_patch(cpart)
    return cpart


# Fonction pour avancer d'un pas de temps et gérer les collisions et les rebonds
def suivant_anim(particules, suivi, dt, ax):
    choc(particules)
    for p in particules:
        p.choc_rebord()
    for p in particules:
        p.avance(dt)
    circles = []
    if suivi:
        n = 0
        for p in particules:
            if n == 0:  # Tracé de la particule dont on suit la trajectoire
                circles.append(Trace_particule_exception(p, ax))
            else:
                circles.append(Trace_particule(p, ax))
            n += 1
    else:
        for p in particules:
            circles.append(Trace_particule(p, ax))
    return circles


# Fonction pour placer aléatoirement des particules sans collision


def place_particules(N_particules, r, v_ini):
    particules = []
    n = 0
    while n < N_particules:
        p = particule_alea(rayon=r, v=v_ini)
        # Vérification des collisions avec les particules existantes
        collision_detected = any(p.est_en_collision(existing_p)
                                 for existing_p in particules)
        if not collision_detected:
            particules.append(p)
            n += 1
    return particules

# Fonction pour gérer les collisions entre les particules


def choc(particules):
    for i in range(len(particules)):
        for j in range(i + 1, len(particules)):
            particules[i].collision(particules[j])

# Fonction pour tracer une particule sur le graphique


def Trace_particule(p, ax):
    circle = Circle((p.x, p.y), radius=p.r)
    ax.add_patch(circle)
    return circle

# Fonction pour extraire les données des particules


def extraction_donnees(particules):
    dt = 0.01
    choc(particules)
    for p in particules:
        p.choc_rebord()
    for p in particules:
        p.avance(dt)
    return particules
