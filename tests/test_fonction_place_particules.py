from brownian_motion.visualization.fonctions_auxiliaires import *
from pytest import *

def test_place_particules():
    N=10
    res=place_particules(N,0.05,1)
    assert len(res)==10
    assert res[0].est_en_collision(res[-1])==False
