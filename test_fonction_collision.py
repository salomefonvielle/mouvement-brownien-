from interface_graphique.definitions_objets import *
from pytest import *

def test_prise_comptes_choc():
    p1=Particule(0.4,0.5,r=0.1)
    p2=Particule(0.45,0.5,r=0.1)
    p1.collision(p2)
    p1.avance
    p2.avance
    assert p1.distance(p2)> p1.r + p2.r