############# imports ##############
import tkinter
# pour la liaison entre matplotlib et tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# pour l'animation, faite avec matplotlib
from brownian_motion.visualization.animation_graphique import *
from brownian_motion.visualization.gazparfaits_graphique import *
from brownian_motion.visualization.animation_particules import *


def genere_animation(widget, N, r, temperature, suivi):
    v_ini = np.sqrt(3 * 1.38*10**(-23)*temperature / (4.6*10**(-20)))
    fig, animation1, init, dt = animation_part(N, r, v_ini, suivi)  # au début j'avais animation_part

    ani = animation.FuncAnimation(
        fig, animation1, init_func=init, frames=800, interval=dt, repeat=False)

    # interface de dessin tkinter
    canvas = FigureCanvasTkAgg(fig, master=widget)
    canvas.draw()

    # création de la barre d'outils

    toolbar = NavigationToolbar2Tk(canvas, widget, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)  # placement de toolbar
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def genere_graph(widget, N, r, temperature):
    v_ini = np.sqrt(3 * 1.38*10**(-23)*temperature / (4.6*10**(-20)))
    fig, prepare_animation, bar_container = animation_graph(N, r, v_ini)

    ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                                  repeat=False, blit=True)
    canvas = FigureCanvasTkAgg(fig, master=widget)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, widget, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)  # placement de toolbar
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def affiche_anim(N, r, v_ini, suivi):
    global frameAnim
    frameAnim.destroy()
    frameAnim = tkinter.Frame(root)
    frameAnim.pack(side='left')
    genere_animation(frameAnim,  N, r, v_ini, suivi)


def affiche_graph(N, r, v_ini):
    global frameAnim
    frameAnim.destroy()
    frameAnim = tkinter.Frame(root)
    frameAnim.pack(side='left')
    genere_graph(frameAnim, N, r, v_ini)


def verif_loi(N, r, T):
    global frameAnim
    frameAnim.destroy()
    frameAnim = tkinter.Frame(root)
    frameAnim.pack(side='left')
    fig = courbe_GP(N, r, T)
    canvas = FigureCanvasTkAgg(fig, master=frameAnim)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frameAnim, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)  # placement de toolbar
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    pass


if __name__ == "__main__":
    ####### creation root window Tkinter ################

    root = tkinter.Tk()  # créer un widget Tk racine
    # lui donner un titre
    root.title("Mouvement Brownien")

    ############### parameters initialisation ##############

    # création d'une fenêtre pour contenir les différents outils associés à l'initialisation des paramètres
    frameBoutons = tkinter.Frame(root)
    frameBoutons.pack(side='right')  # placement: sur la droite
    frameAnim = tkinter.Frame(root)
    frameAnim.pack(side='left')

    # bouton pour arrêter l'animation et fermer a fenêtre
    quitter = tkinter.Button(master=frameBoutons, text="Quitter",
                             command=quit,  borderwidth=2, relief=tkinter.GROOVE)
    # placement de ce bouton au bas de la fenêtre
    quitter.pack(side=tkinter.BOTTOM)
    # création d'un slider dans la fenêtre créée précédemment
    temperature = tkinter.Scale(frameBoutons, from_=0, to=10000, resolution=5,
                                orient='horizontal', label='Température (en K)',  borderwidth=2)
    temperature.set(300)
    temperature.pack()  # placement du slider dans la fenêtre

    rayon = tkinter.Scale(frameBoutons, from_=0, to=3,
                          orient='horizontal', resolution=0.1, label="Rayon des particules",  borderwidth=2)
    rayon.set(1)
    rayon.pack()  # placement du slider dans la fenêtre

    nbParticules = tkinter.Scale(
        frameBoutons, from_=1, to=1000, orient='horizontal', label='Nombre de particules')
    nbParticules.set(50)
    nbParticules.pack()

    suivi = tkinter.BooleanVar()
    checkBox = tkinter.Checkbutton(
        frameBoutons, variable=suivi, text="Trajectoire d'une particule", onvalue=1, offvalue=0)
    checkBox.pack()

    lancementSim = tkinter.Button(frameBoutons, text='Démarrer la simulation',
                                  command=lambda: affiche_anim(nbParticules.get(), rayon.get()/100, temperature.get(), suivi.get()), borderwidth=2, relief=tkinter.GROOVE)
    lancementSim.pack()  # création d'un bouton qui, une fois cliqué, lance la fonction d'animation, en donnant en entrée les paramètres récupérés

    lancementGraph = tkinter.Button(frameBoutons, text='Démarrer le graphique',
                                    command=lambda: affiche_graph(nbParticules.get(), rayon.get()/100, temperature.get()), borderwidth=2, relief=tkinter.GROOVE)
    lancementGraph.pack()  # création d'un bouton qui, une fois cliqué, lance la fonction d'animation, en donnant en entrée les paramètres récupérés

    verifierLDGP = tkinter.Button(frameBoutons, text='Vérifier la loi des gaz parfaits',
                                  command=lambda: verif_loi(nbParticules.get(), rayon.get()/100, temperature.get()), borderwidth=2, relief=tkinter.GROOVE)
    verifierLDGP.pack()  # création d'un bouton qui, une fois cliqué, lance la fonction d'animation, en donnant en entrée les paramètres récupérés

    root.protocol("WM_DELETE_WINDOW", quit)
    tkinter.mainloop()  # lancement de la simulation
