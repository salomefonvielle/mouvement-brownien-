import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from random import random
    
def marche_aleatoire(nb_iterations=1000,rayon=0.02,vitesse=1,dt=0.03):
    
    #x_ini, y_ini = rayon + (1 - 2 * rayon) * np.random.random(2) # enceinte de dimensions (1,1)
    x_ini, y_ini = 0.5, 0.5    #particule au centre au départ 
    patch = plt.Circle((x_ini, y_ini), rayon) # cercle initial
    
    pos_x,pos_y=[x_ini],[y_ini] # initialisation des listes des positions prises successivement par la particule
    x,y=x_ini,y_ini
    
    for i in range(nb_iterations): # incrémenter les valeurs de position
        angle=2*np.pi*random()      #on prend un angle aléatoire entre 0 et 2pi
        x+=np.cos(angle)*vitesse*dt # projection selon x du chemin parcouru pendant dt
        y+=np.sin(angle)*vitesse*dt
        pos_x.append(x)   #on crée les listes contenant les positions successives
        pos_y.append(y)
        
    def init():                          #initialisation de la particule
        patch.center = (x_ini,y_ini)
        ax.add_patch(patch)
        return patch,
    
    def animate(i):                      
        x, y = patch.center
        x = pos_x[i]
        y = pos_y[i]
        patch.center = (x, y)
        line.set_data(pos_x[:i], pos_y[:i])    #on trace le trajet de la particule
        return patch,line
        
    fig = plt.figure() # création d'une figure vide
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 1), ylim=(0, 1))  # création d'un sous graphique, désactivation de l'échelle automatique des axes et précision de cette échelle
    line, = ax.plot([],[], color='blue')
    ax.set_aspect('equal') # même échelle pour x et y
    plt.xlabel('x-direction') # titre axe des abscisses 
    plt.ylabel('y-direction') # titre axe des ordonnées
    plt.title("Marche aléatoire d'une particule") # titre de la figure

    ani = animation.FuncAnimation(fig, animate, range(1, len(pos_x)),interval=100, blit=True,init_func=init) # fonction qui permet de créer animation avec en argument la figure dans laquelle on crée l'animation, fonction appelée à chaque itération pour mettre à jour la figure, blint pour intervalle de temps et init la fonction d'initialisation appelée au début de l'animation
    plt.show() # affichage de la figure
    
if __name__=="__main__":  
    marche_aleatoire()
