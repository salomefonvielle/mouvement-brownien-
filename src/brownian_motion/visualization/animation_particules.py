# Module pour générer la simulation des particules dans le cadre

# Importation des modules nécessaires
import matplotlib.pyplot as plt
from brownian_motion.physics.fonctions_auxiliaires import *

# Définition de la fonction d'animation pour les particules


def animation_part(N, r, v_ini, suivi):
    # Initialisation des listes de positions de la particule que l'on suit
    xp = []
    yp = []

    # Placement initial des particules
    L = place_particules(N, r, v_ini)

    # Fonction d'initialisation de l'animation
    def init():
        global circles
        circles = []
        for circle in circles:
            circle.remove()

        new_circles = [Trace_particule(i, ax) for i in L]
        circles.extend(new_circles)
        return circles

    # Fonction d'animation principale
    def animation(i):
        global circles
        time_text.set_text(time_template % (i * dt))
        for circle in circles:
            circle.remove()
        circles = suivant_anim(L, suivi, dt, ax)
        if suivi:
            line, = ax.plot([], [], color='blue')
            # Ajout des positions successives de la particule observée
            xp.append(L[0].x)
            yp.append(L[0].y)
            line.set_data(xp[:i], yp[:i])
            return circles, time_text, line  # Tracé
        else:
            return circles, time_text

    # Création de la figure et du sous-graphique
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 1), ylim=(0, 1))
    ax.set_aspect('equal')  # Même échelle pour x et y
    plt.xlabel('x-direction')  # Nom de l'axe des x
    plt.ylabel('y-direction')  # Nom de l'axe des y
    plt.title('Particules dans une enceinte')  # Titre de la figure
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    dt = 0.005

    # Retourne la figure, la fonction d'animation, la fonction d'initialisation et le pas de temps
    return fig, animation, init, dt
