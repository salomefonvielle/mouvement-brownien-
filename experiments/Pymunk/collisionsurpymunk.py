import sys, random
import pygame
import pymunk
import pymunk.pygame_util


pygame.init()               
display=pygame.display.set_mode((500,500))    #initialisation de la fenêtre
clock=pygame.time.Clock()
space=pymunk.Space()
pygame.display.set_caption('Collision de "petites" particules')

class Ball():     #création de la classe des particules
    def __init__(self,x,y):
        self.body=pymunk.Body()
        self.body.position=x,y
        self.shape=pymunk.Circle(self.body,10)
        self.body.velocity = random.uniform(-50,50),random.uniform(-50,50)
        self.shape.elasticity = 1
        self.shape.density = 1
        space.add(self.body, self.shape)
    def draw(self):       #dessine les particules
        pygame.draw.circle(display,(255,0,0), self.body.position,10)


Balls=[]
for i in range(1,100):         #positions initiales aléatoires des particules
    x=random.randint(1,500)
    y=random.randint(1,500)
    Balls.append(Ball(x,y))

def simulation():
    while True:            #interface de la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        for i in range(len(Balls)):
            Balls[i].draw()

        pygame.display.update()
        clock.tick(50)         #au plus 50 images par seconde
        space.step(1/50)

simulation()
pygame.quit()



        




