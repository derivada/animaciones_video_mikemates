from manim import *
from numpy import *
from utils import *

fs = 32
# Sección 5.1
class manim_12(Scene):
    def construct(self):        
        # dibujar polinomios
        grid = mostrar_grid(self)
        pol1 = grid.plot(lambda x: x**2 - 2, color = GREEN)
        label1 = grid.get_graph_label(pol1, "x^2 - 2", x_val = -2, direction = DL)
        
        pol2 = grid.plot(lambda x: 2*x**4 - 3*x**3 - x + 1, color = BLUE)
        label2 = grid.get_graph_label(pol2, "2x^4 - 3x^3 - x + 1", x_val = 2, direction = DR*1.5)
        
        pol3 = grid.plot(lambda x: x**5 - x + 1, color = RED)
        label3 = grid.get_graph_label(pol3, "x^5 - x + 1", x_val = -3/2, direction = LEFT)
        
        self.play(AnimationGroup(Create(pol1, run_time = 3), DrawBorderThenFill(label1), lag_ratio = 0.5))
        self.wait(1)
        self.play(AnimationGroup(Create(pol2, run_time = 3), DrawBorderThenFill(label2), lag_ratio = 0.5))
        self.wait(1)
        self.play(AnimationGroup(Create(pol3, run_time = 3), DrawBorderThenFill(label3), lag_ratio = 0.5))
        self.wait(3)
        
        # raíces
        pol1_r1, pol1_r2 = Dot([-sqrt(2), 0.0, 0.0], color = GREEN), Dot([sqrt(2), 0.0, 0.0], color = GREEN)
        pol2_r1, pol2_r2 = Dot([0.6045, 0.0, 0.0], color = BLUE), Dot([1.5736, 0.0, 0.0], color = BLUE)
        pol3_r1 = Dot([-1.1673, 0.0, 0.0], color = RED)
        roots_group = VGroup(pol1_r1, pol3_r1, pol2_r1, pol1_r2, pol2_r2)
        self.play(AnimationGroup(*[FadeIn(root) for root in roots_group], lag_ratio = 0.5, run_time = 2))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(pol1), FadeOut(label1), FadeOut(pol2), FadeOut(label2), FadeOut(pol3), FadeOut(label3), lag_ratio = 0.2, run_time = 2))
        self.wait(2)
        self.play(AnimationGroup(*[Indicate(root) for root in roots_group], lag_ratio = 0.2))
        
        alg_pos = [-3.0, -2.0, 0.0]
        for root in roots_group:
            arrow = Line(start = alg_pos, end = root.get_center(), color = root.get_color())
            self.play(FadeIn(arrow), run_time = 0.5)
        alg = Text("Números algebraicos", t2c = {"algebraicos": YELLOW}, font_size = fs).next_to(alg_pos, DOWN/2)
        self.wait(1)
        self.play(DrawBorderThenFill(alg), run_time = 2)
        self.wait(3)