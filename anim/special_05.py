from manim import *
from numpy import *
from utils import *

fs = 48

# Sección 6.3
class special_05(Scene):
    def construct(self):    
        ramanujan = Tex("Aproximación del problema en 1914", font_size=32)
        ramanujan_2 = Tex("con 8 decimales", font_size = 32).next_to(ramanujan, DOWN)
        ramanujan_full = VGroup(ramanujan, ramanujan_2)
        self.play(Write(ramanujan_full), run_time = 2.5)
        self.wait(3)