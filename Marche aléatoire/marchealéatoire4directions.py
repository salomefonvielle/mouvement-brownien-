import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
from random import random
import numpy as np



x=0.5   #position initiale de la particule
y=0.5

pos_x=[0.5] # positions prises par la particule au cours du temps
pos_y=[0.5 ]

for i in range(1000):      #on crée les positions successives de la particule aléatoirement
    a = randint(0,3)
    if a == 0:
        x += 0.01
    elif a == 1:
        x -= 0.01
    elif a == 2:
        y += 0.01
    else:
        y -= 0.01
    pos_x.append(x)
    pos_y.append(y)

    

dt = 0.1  #intervalle entre 2 positions
    
fig = plt.figure() # création d'une figure vide
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 1), ylim=(0, 1))  # création d'un sous graphique, désactivation de l'échelle automatique des axe et précision de cette échelle
ax.set_aspect('equal') # même échelle pour x et y
plt.xlabel('x-direction') # titre axe des abscisses 
plt.ylabel('y-direction') # titre axe des ordonnées
plt.title("Marche aléatoire d'une particule") # titre de la figure


line, = ax.plot([],[], color='blue')
particule, = ax.plot([], [], 'bo', lw=2, markersize=10) # 'bo' correspond à un cercle bleu, 10 correspons à la taille de la particule 
time_template = 'time = %.1fs' # chaine de formatage avec nombre de chiffre après la virgule du flottant, chaîne de caractère.
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes) # ajout texte avec coordonnées données sous forme normalisée, contenu du texte, on précise que les coordonnées sont normalisées 
 
def animate(i): # évolution des données au cours du temps
        particule.set_data([pos_x[i]], [pos_y[i]]) # représentation de la particule au cours du temps
        line.set_data(pos_x[:i], pos_y[:i])
        time_text.set_text(time_template % (i*dt)) # évolution du temps
        return particule, line, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(pos_x)),interval=100, blit=True) # fonction qui permet de créer animation avec en argument la figure dans laquelle on crée l'animation, fonction appelée à chaque itération pour mettre à jour la figure, blint pour intervalle de temps et init la fonction d'initialisation appelée au début de l'animation
plt.show() # affichage de la figure 