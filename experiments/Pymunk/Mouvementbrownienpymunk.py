import sys, random
import pygame
import pymunk
import pymunk.pygame_util

#on crée l'interface
pygame.init()
display=pygame.display.set_mode((500,500))  #avec taille de la fenêtre
clock=pygame.time.Clock()      #on crée une référence de temps pour le nombre d'images par seconde
space=pymunk.Space()
pygame.display.set_caption('Mouvement brownien sur pymunk')  #titre de la fenêtre

#on crée une classe pour les particules
class Ball():
    def __init__(self,x,y,radius):
        self.body=pymunk.Body()
        self.body.position=x,y    #position initiale de la particule
        self.shape=pymunk.Circle(self.body,radius)  
        self.body.velocity = random.uniform(-150,150),random.uniform(-150,150)   #vitesse initiale prise aléatoirement
        self.shape.elasticity = 1  #conservation quantité de mouvement
        self.shape.density = 1
        space.add(self.body, self.shape)
    

Balls=[]
for i in range(1,500):         #création de 500 particules
    x=random.randint(1,500)    #on place des particules de manière aléatoire
    y=random.randint(1,500)
    radius=6                   #rayon de la particule
    Balls.append(Ball(x,y,radius))
Balls.append(Ball(255,255,19))    #ajout de la grosse particule

#création des bords
def add_bord(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)   #objet de type "STATIC"
    body.position = (0,0)
    l1 = pymunk.Segment(body, (0, 0), (0, 500), 5.0)   #on crée successivement les 4 bords, prend en argument les deux poinrs à relier et l'epaisseur du bord
    l2 = pymunk.Segment(body, (500,0), (0, 0), 5.0)
    l3 = pymunk.Segment(body, (0,500), (500, 500), 5.0)
    l4 = pymunk.Segment(body, (500,500), (500, 0), 5.0)
    l1.friction = 1   #frottement sur les bords"
    l2.friction = 1
    l3.friction = 1
    l4.friction = 1
    l1.elasticity =1   #rebond sur les bords, type conservation quantité mouvement
    l2.elasticity = 1
    l3.elasticity = 1
    l4.elasticity = 1
    

   
    space.add(l1, l2,l3,l4,body)  #on ajoute les bords à notre espace
    return l1,l2,l3,l4



lines = add_bord(space)

#animation 
def simulation():
    while True:
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:     #fermeture de la fenêtre
                return
        display.fill((255,255,255))      #(255,255,255) correspond à un fond blanc                      
        draw_options = pymunk.pygame_util.DrawOptions(display) #on affiche tous les différents corps
        space.debug_draw(draw_options)
        pygame.display.update()
        clock.tick(50)    #au plus 50 images par seconde
        space.step(1/50)  #temps entre 2 images

simulation()
pygame.quit()