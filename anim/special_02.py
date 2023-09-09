from manim import *
from numpy import *
from utils import *

fs = 24
liou_color = BLUE
euler_color = GREEN
config.background_color = LIGHTER_GRAY
Tex.set_default(color=BLACK)

# Sección 1.3
class special_02(Scene):
    def construct(self):    
        ko = Tex("Kochański, 1685", font_size = 48).move_to([3.0, 1.5, 0.0])
        ko_approx = Tex("4 dígitos de precisión", font_size = 32, color = DARKER_GRAY).next_to(ko, DOWN).align_to(ko, LEFT)
        ra = Tex("Ramanujan, 1914", font_size = 48).move_to([-3.0, -1.5, 0.0])
        ra_approx = Tex("8 dígitos de precisión", font_size = 32, color = DARKER_GRAY).next_to(ra, DOWN).align_to(ra, RIGHT)
        self.play(DrawBorderThenFill(ko))
        self.play(FadeIn(ko_approx))
        self.wait(1)
        self.play(DrawBorderThenFill(ra))
        self.play(FadeIn(ra_approx))
        self.wait(2)