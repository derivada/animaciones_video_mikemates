from manim import *
from numpy import *
from utils import *

fs = 24
liou_color = BLUE
euler_color = GREEN

# Sección 1.2
class special_01(Scene):
    def construct(self):    
        quad = Square(side_length = sqrt(pi), color = RED).move_to([-2.0, 0.0, 0.0])
        circ = Circle(radius = 1, color = BLUE).move_to([2.0, 0.0, 0.0])
        self.play(Create(quad), Create(circ))
        self.wait(2)
        equal = Tex("=", font_size = fs*2, color = WHITE)
        arrow = Vector(UP).next_to(equal, DOWN)
        equal_text = Tex("Áreas iguales", font_size = fs*1.5, color = WHITE).next_to(arrow, DOWN)
        self.play(quad.animate.set_fill(color = RED, opacity = 0.5), circ.animate.set_fill(color = BLUE, opacity = 0.5), )
        self.wait(2)
        self.play(FadeIn(equal), FadeIn(arrow), DrawBorderThenFill(equal_text))
        self.wait(3)