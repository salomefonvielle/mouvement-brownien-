#Défintion d'une classe pour les particules 

import numpy as np
from random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import uniform

# On se placera toujours dans une enceinte de dimensions (1,1)

class Particule():
    def __init__(self,x,y,angle=0,r=5, masse=1,vitesse=1):
        self.x=x # abscisse de la particule
        self.y=y # ordonnée
        self.angle=angle # angle en radians compté dans le sens trigonométrique depuis l'axe (Ox), caractérise la direction de la particule
        self.r=r # rayon
        self.mass=masse # masse            
        self.vitesse=vitesse # norme de la vitesse    
        self.vx=vitesse*np.cos(angle) # composante de la vitesse selon x
        self.vy=vitesse*np.sin(angle) # composante de la vitesse selon y
    
    def rebord(self):
        """ retourne un tuple:
        (True,"top") si la particule est sur le bord haut
        (True,"left") si la particule est sur le bord gauche
        ...
        (False,None) si la particule n'est pas sur un bord

        """
        if self.x+self.r>1: # si la particule dépasse du bord droit
            return (True,"right")
        elif self.x-self.r<0:
            return (True,"left")
        elif self.y+self.r>1:
            return (True,"top")
        elif self.y-self.r<0:
            return (True,"bottom")
        return (False,None) # si la particule ne touche aucun bord
        
    def est_en_collision(self,autre_part):
        """caractérise la collision

        Args:
            autre_part (Particule()): autre particule

        Returns:
            bool: True si les 2 particules (self et autre_part) sont en collision, False sinon
        """
        return self.distance(autre_part)<self.r + autre_part.r # True si les 2 particules se superposent en partie
    
    
    # Modèle de prise en compte des chocs abandonné par la suite:
    
    # def collision_boltzmann (self,autre_part):
    #     """modifie la vitesse des deux particules si elles se choquent selon le modèle de Boltzmann

    #     Args:
    #         autre_part (Particule()): autre particule
    #     """
    #     if self.est_en_collision(autre_part)==True: # s'il y a collision entre les deux particules
    #         p1=self.vitesse*self.mass #normes des quantités de mvt des particules
    #         p2=autre_part.vitesse*autre_part.mass

    #         #calcul de pG et pR0 et PR
    #         x_pG= 0.5*(p1*np.cos(self.angle)+p2*np.cos(autre_part.angle)) #coordonnées de p_G la moyennne des qtés de mvt
    #         y_pG=0.5*(p1*np.sin(self.angle)+p2*np.sin(autre_part.angle))
            
    #         x_pR0= 0.5*(p1*np.cos(self.angle)-p2*np.cos(autre_part.angle)) #coordonnées de p_G la moyennne des qtés de mvt
    #         y_pR0=0.5*(p1*np.sin(self.angle)-p2*np.sin(autre_part.angle))
    #         pR0=np.sqrt((x_pR0)**2+(y_pR0)**2)  #norme de pR
            
    #         theta=uniform(0.5*np.pi,1.5*np.pi) #2*np.pi*random() #angle de pR'
    #         x_pR=pR0*np.cos(theta)  #nouvelles coordonnées de pR après le choc
    #         y_pR=pR0*np.sin(theta)

    #         #modification de la particule 1 pour prendre en compte les effets du choc
    #         x_p1c=x_pG+x_pR   #coordonnées de la qté de mvt de la particule 1 après le choc
    #         y_p1c=y_pG+y_pR
    #         p1c=np.sqrt((x_p1c)**2+(y_p1c)**2) #norme de la qté de mvt de la particule 1 après le choc

    #         if y_p1c>0:
    #             angle1=np.arccos(x_p1c/p1c)
    #         else:
    #             angle1=-np.arccos(x_p1c/p1c)#+ np.pi
            
    #         v1= p1c/self.mass
            
    #         #modification de la particule 2 pour prendre en compte les effets du choc
    #         x_p2c=x_pG-x_pR   #coordonnées de la qté de mvt de la particule 1 après le choc
    #         y_p2c=y_pG-y_pR
    #         p2c=np.sqrt((x_p2c)**2+(y_p2c)**2) #norme de la qté de mvt de la particule 1 après le choc

    #         if y_p2c>0:
    #             angle2=np.arccos(x_p2c/p2c)
    #         else:
    #             angle2=np.arccos(x_p2c/p2c)+ np.pi
            
    #         v2= p2c/autre_part.mass
            
    #         self.vitesse=v1
    #         self.angle=angle1
    #         self.vx=self.vitesse*np.cos(self.angle)
    #         self.vy=self.vitesse*np.sin(self.angle)
    #         autre_part.angle,autre_part.vitesse=angle2,v2
    #         autre_part.vx=autre_part.vitesse*np.cos(autre_part.angle)
    #         autre_part.vy=autre_part.vitesse*np.sin(autre_part.angle)
            
    def collision(self,autre_part):
        """modifie la vitesse des deux particules si elles sont en collision

        Args:
            autre_part (Particule()): autre particule
        """
        if self.est_en_collision(autre_part)==True: # s'il y a collision entre les deux particules
            M=self.mass+autre_part.mass # somme des masses des deux particules
            delta_v=np.array([self.vx-autre_part.vx,self.vy-autre_part.vy]) # vecteur différence de vitesse des deux particules
            delta_position=np.array([self.x-autre_part.x,self.y-autre_part.y]) # vecteur différence de position entre les deux particules
            carre_distance=np.dot(delta_position,delta_position) # carré de la distance séparant les particules
            R=self.r+autre_part.r # somme des rayons des deux particules
            
            # modification des vitesses des deux particules telles que la quantité de mouvement est conservée:
            self.vx-=2*autre_part.mass/M * np.dot(delta_v,delta_position)/carre_distance * (self.x-autre_part.x)
            self.vy-=2*autre_part.mass/M * np.dot(delta_v,delta_position)/carre_distance * (self.y-autre_part.y)
            autre_part.vx-=2*self.mass/M * np.dot(delta_v,delta_position)/carre_distance * (autre_part.x-self.x)
            autre_part.vy-=2*self.mass/M * np.dot(delta_v,delta_position)/carre_distance * (autre_part.y-self.y)
            
            # modification de la position de l'une des deux particules, telles qu'elles soient tangentes, pour éviter l'effet de "collage" dans l'animation
            autre_part.x=self.x+R*(autre_part.x-self.x)/np.sqrt(carre_distance)
            autre_part.y=self.y+R*(autre_part.y-self.y)/np.sqrt(carre_distance)
    
    def choc_rebord(self):
        """modifie la vitesse de la particule self s'il y a choc sur une paroi de l'enceinte, et sa position
        """
        if self.rebord()[1]!=None: # s'il y a choc contre un rebord
            reb=self.rebord()[1] # variable qui contient la paroi concernée par le choc
            if reb=="right":
                self.vx*=-1
                self.x=1-self.r # on modifie aussi la position de la particule pour éviter les chocs à répétition; on la place telle qu'elle soit tangente au bord correspondant
            elif reb=="left":
                self.vx*=-1
                self.x=self.r
            elif reb=="bottom":
                self.vy*=-1
                self.y=self.r
            else:
                self.vy*=-1
                self.y=1-self.r
                
    def avance(self,dt):
        """modifie la position de la particule

        Args:
            dt (float): intervalle de temps entre deux mises à jour
        """
        self.x+=self.vx*dt
        self.y+=self.vy*dt   

    def distance(self,p2):
        return np.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
             

def particule_alea(rayon=0.05,v=0.1):
    """ "crée" une particule à un endroit aléatoire dans l'enceinte, qui a une direction aléatoire

    Args:
        e (Enceinte())

    """
    return Particule(random(),random(),2*np.pi*random(),r=rayon,vitesse=v)  





    







