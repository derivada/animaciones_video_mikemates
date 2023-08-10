from manim import *
from numpy import *

fs = 36

# Sección 3.1
class manim_08(Scene):
    def construct(self):        
        # puntos A y B
        # angulo = 45º, A = 3, B = 2, base_len = 2
        p0_coords, p1_coords = [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0]
        pA_coords, pB_coords,  pAE_coords = [5.0, 0.0, 0.0], [-1.0 + 2*sqrt(2), 2*sqrt(2), 0.0], [3.0, 2.0, 0.0]