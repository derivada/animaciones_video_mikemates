from manim import *
from numpy import *
from utils import *

fs = 60
color_constr, color_constr_2 = BLUE, WHITE
color_poly, color_poly_2 = RED, WHITE

# Sección 5.6
class manim_15(Scene):
    def construct(self):
        constr_title = Text("Números construibles", font_size = fs*0.66, font = "Arial", color = color_constr).move_to([-3.5, 3.0, 0.0])
        poly_title = Text("Polinomios donde son raíz", font_size = fs*0.66, font = "Arial", color = color_poly).move_to([3.5, 3.0, 0.0])
        title_group = VGroup(constr_title, poly_title)
        line = Line(constr_title.get_boundary_point(LEFT) + LEFT/4, poly_title.get_boundary_point(RIGHT) + RIGHT/4).next_to(title_group, DOWN)

        constr_1 = Tex(r"$3$", font_size = fs, color = color_constr_2).next_to(constr_title, DOWN*3)
        poly_1 = Tex(r"$x - 3$", font_size = fs, color = color_poly_2).next_to(poly_title, DOWN*3)
        constr_2 = Tex(r"$\sqrt{2} + 1$", font_size = fs, color = color_constr_2).next_to(constr_1, DOWN*2)
        poly_2 = Tex(r"$(x - 1)^2 - 2$", font_size = fs, color = color_poly_2).next_to(poly_1, DOWN*2)
        constr_3 = Tex(r"$\frac{2}{3} + \sqrt{1 + \sqrt{2}}$", font_size = fs, color = color_constr_2).next_to(constr_2, DOWN*2)
        poly_3 = Tex(r"$((x - \frac{2}{3})^2 - 1)^2 - 2$", font_size = fs, color = color_poly_2).next_to(poly_2, DOWN*2)

        self.play(FadeIn(constr_title), FadeIn(poly_title), Create(line), run_time = 2)
        self.wait(2)
        self.play(DrawBorderThenFill(constr_1), DrawBorderThenFill(poly_1))
        self.wait(2)
        self.play(DrawBorderThenFill(constr_2), DrawBorderThenFill(poly_2))
        self.wait(2)
        self.play(DrawBorderThenFill(constr_3), DrawBorderThenFill(poly_3))
        self.wait(3)