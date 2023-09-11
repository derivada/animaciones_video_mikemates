from manim import *
from numpy import *
from utils import *

fs = 48

# Sección 6.3
class special_04(Scene):
    def construct(self):    
        lindemann = Tex("Prueba que $\pi$ es transcendental en 1882,", font_size=32)
        lindemann_2 = Tex("completando el puzzle de la cuadratura del círculo", font_size = 32).next_to(lindemann, DOWN)
        lindemann_full = VGroup(lindemann, lindemann_2)
        self.play(Write(lindemann_full), run_time = 2.5)
        self.wait(3)