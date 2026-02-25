# from collisions_particules import *
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import random
# import numpy as np
# from matplotlib.patches import Circle

from physics.fonctions_auxiliaires import *


def courbe_GP(N, r, T):
    # N=100
    # r=0.01
    # T=300
    v_ini = np.sqrt((3*1.38*(10**(-23))*T)/(4.6*10**(-20)))

    dt = 0.01
    delta_t = 1

    def creation_bin(dx):
        inter = [0]
        a = 0
        for i in range(int(10/dx)):
            a += dx
            inter.append(a)
        return inter

    def calcul_norme_vitesse(particules_at):
        listeV = []
        for p in particules_at:
            listeV.append(np.sqrt(p.vx**2+p.vy**2))
        return listeV

    L = place_particules(N, r, v_ini)

    '''
    def prepare_animation(bar_container):
        def animate(frame_number):
            data = calcul_norme_vitesse(extraction_donnees(L))
            n, _ = np.histogram(data, creation_bin(0.1))
            for count, rect in zip(n, bar_container.patches):
                rect.set_height(count)
            return bar_container.patches
        return animate


    fig, ax = plt.subplots()
    _, _, bar_container = ax.hist(calcul_norme_vitesse(L), creation_bin(0.1), lw=1,
                                ec="black", fc="black", alpha=0.5)
    ax.set_ylim(top=200)  
    ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                                repeat=False, blit=True)

    '''

    def vitesse_quadratique(particules):
        P = calcul_norme_vitesse(particules)
        V = 0
        for i in range(len(P)):
            V += (P[i])
        return ((1/(len(P)))*V*1000)

    def pression_cinetique_reelle(particules):
        mN2 = 4.6*(10)**(-26)
        return ((1/3)*mN2*(N*10**22)*vitesse_quadratique(particules)**2)

    x = [i for i in range(1, T, 30)]
    y = [pression_cinetique_reelle(place_particules(
        N, r, np.sqrt((3*1.38*(10**(-23))*i)/(4.6*10**(-20))))) for i in x]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, y, 'x')
    m, b = np.polyfit(x, y, 1)
    # print(m, b)
    R = m*6.02*10**(23)/(N*10**(22))
    ax.text(10, plt.ylim()[1]*0.9, f"R = {R: .2f}")
    ax.set_xlabel("Température (en K)")

    kB = 1.38*10**(-23)

    return fig

    '''def f_boltzmann(v,T,m):
        V=v*1000
        m=4.6*10**(-26)
        return N*4*np.pi*(m/(2*np.pi*kB*T))**(3/2)*V**2*np.exp((-m*v**2/(2*kB*T)))

    a=0
    X=[]
    for i in range (1000):
        X.append(a)
        a+=0.01
        

    Y=[f_boltzmann(v,300,4.6*10**(-26)) for v in X]

    plt.plot(X,Y)
    plt.show()'''
