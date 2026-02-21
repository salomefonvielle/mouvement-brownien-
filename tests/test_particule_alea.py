from brownian_motion.visualization.definitions_objets import *
from pytest import *
import numpy as np

def test_alea():
    p=particule_alea()
    assert round(np.sqrt(p.vx**2 + p.vy**2),3)==0.1
    
    