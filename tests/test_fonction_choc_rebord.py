from physics.definitions_objets import *
from pytest import *

def test_choc_rebord():
    rayon=0.05
    #p=[np.array([0.5,0]),np.array([0,1]),r,1] 
    p=Particule(0.5,rayon-0.01,angle=-np.pi/4,vitesse=1,r=rayon) # au milieu en bas de l'enceinte
    p.choc_rebord()
    assert p.vy>0 # la particule doit repartir vers le haut
    p=Particule(rayon-0.01,0.5,angle=-3*np.pi/4,vitesse=1,r=rayon) # au milieu à gauche de l'enceinte
    p.choc_rebord()
    assert p.vx>0 # la particule doit repartir vers la droite
    p=Particule(1.01-rayon,0.5,angle=0,vitesse=1,r=rayon) # au milieu à droite de l'enceinte
    p.choc_rebord()
    assert p.vx<0 # la particule doit repartir vers la gauche
    p=Particule(0.5,1.01-rayon,angle=np.pi/4,vitesse=1,r=rayon) # au milieu en haut de l'enceinte
    p.choc_rebord()
    assert p.vy<0
    
