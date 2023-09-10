from manim import *
from numpy import *
from utils import *

fs = 40
circ_color = BLUE
sq_color, sq_fill_op = RED, 0.5

# Sección 4.9
class manim_11(MovingCameraScene):
    def construct(self): 
        self.camera.frame.set_width(12.0)       
        mostrar_grid(self)
        self.wait(3)
        circ = Circle(color = circ_color)
        area_circ = Tex(r"$\pi$", font_size = fs, color = circ_color).shift(UR*0.9)
        sq = Square(sqrt(pi), color = RED, fill_opacity = sq_fill_op).shift(UL * sqrt(pi)/2)
        side_sq_up = Tex(r"$\sqrt{\pi}$", font_size = fs, color = sq_color).next_to(sq, UP/2)
        side_sq_left = side_sq_up.copy().next_to(sq, LEFT/2)
        pregunta = Tex(r"¿Podemos construir $\sqrt{\pi}$?", font_size = fs, color = YELLOW_D).align_to(sq, UP).shift(RIGHT*3 + UP*0.66)
        pregunta2 = Tex(r"¿Podemos construir $\pi$?", font_size = fs, color = YELLOW_D).align_to(sq, UP).shift(RIGHT*3 + UP*0.66)

        self.play(Create(circ), run_time = 2)
        self.wait(3)
        self.play(Write(area_circ), circ.animate.set_fill(color = circ_color, opacity = 0.5), run_time = 1.5)
        self.wait(3)
        self.play(DrawBorderThenFill(sq), run_time = 2)
        self.wait(3)
        self.play(FadeIn(side_sq_up), FadeIn(side_sq_left))
        self.wait(3)
        self.play(DrawBorderThenFill(pregunta), run_time = 2)
        self.wait(3)
        self.play(Transform(pregunta, pregunta2), run_time = 2)
        self.wait(3)
        self.play(Indicate(pregunta), run_time = 2)
        self.wait(3)