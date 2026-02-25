from physics.definitions_objets import *
from pytest import *


def test_rebord():
    p1=Particule(0.1,0.5,r=0.2)
    assert p1.rebord()==(True,"left")
    p2=Particule(0.9,0.5,r=0.2)
    assert p2.rebord()==(True,"right")
    p3=Particule(0.5,0.1,r=0.2)
    assert p3.rebord()==(True,"bottom")
    p4=Particule(0.5,0.9,r=0.2)
    assert p4.rebord()==(True,"top")
    p5=Particule(0.5,0.5,r=0.2)
    assert p5.rebord()==(False,None)