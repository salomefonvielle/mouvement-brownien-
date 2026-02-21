from interface_graphique.definitions_objets import * 
from pytest import *
import numpy as np

def test_avance():
    p=Particule(0.4,0.5,0,0.1,1)
    dt=0.005
    p.avance(dt)
    assert p.x==0.4+dt
    assert p.y==0.5 