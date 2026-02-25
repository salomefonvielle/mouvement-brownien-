# Graphique répartition des vitesses

from physics.fonctions_auxiliaires import *

# Définition de la fonction d'animation


def animation_graph(N, r, v_ini):
    dt = 0.01
    delta_t = 1

    # Fonction de création des intervalles pour l'histogramme
    def creation_bin(dx):
        inter = [0]
        a = 0
        for i in range(int(10/dx)):
            a += dx
            inter.append(a)
        return inter

    # Fonction pour calculer la norme de la vitesse pour chaque particule
    def calcul_norme_vitesse(particules_at):
        listeV = []
        for p in particules_at:
            listeV.append(np.sqrt(p.vx**2+p.vy**2))
        return listeV

    # Placement initial des particules
    L = place_particules(N, r, v_ini)

    # Fonction pour préparer l'animation
    def prepare_animation(bar_container):
        # Fonction d'animation
        def animate(frame_number):
            # Calcul des normes de vitesse à chaque frame
            data = calcul_norme_vitesse(extraction_donnees(L))
            # Création de l'histogramme
            n, _ = np.histogram(data, creation_bin(0.1))
            # Mise à jour des hauteurs des rectangles de l'histogramme
            for count, rect in zip(n, bar_container.patches):
                rect.set_height(count)
            return bar_container.patches
        return animate

    # Création de la figure et des sous-graphiques
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Création de l'histogramme initial
    _, _, bar_container = ax.hist(calcul_norme_vitesse(L), creation_bin(0.1), lw=1,
                                  ec="black", fc="black", alpha=0.5)

    # Configuration des axes et du titre
    ax.set_ylim(top=200)
    ax.set_xlabel("Vitesse")
    ax.set_ylabel("Nombre de particules")
    ax.set_title("Répartition des vitesses")

    # Retourne la figure, la fonction d'animation préparée, et le conteneur d'histogramme
    return fig, prepare_animation, bar_container
