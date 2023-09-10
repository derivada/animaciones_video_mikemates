from manim import *
from numpy import *
from utils import *

fs = 36

# Sección 4.5
class manim_07(Scene):
    def construct(self):        
        mostrar_grid(self)
        pA_coords, pB_coords, pC_coords, pD_coords, pE_coords = [0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [3.0, 2.0, 0.0], [3.0, 3.0, 0.0], [3.0, 0.0, 0.0] # escalar todo por 2 en coordenadas de manim
        pA, pB, pC, pD, pE = Dot(pA_coords, color = BLUE), Dot(pB_coords, color = BLUE), Dot(pC_coords, color = RED), Dot(pD_coords, color = RED), Dot(pE_coords, color = RED)
        pA_label, pB_label, pC_label, pD_label, pE_label = Tex("A", font_size = fs, color = BLUE).next_to(pA, DL/2), Tex("B", font_size = fs, color = BLUE).next_to(pB, DL/2), Tex("C", font_size = fs, color = RED).next_to(pC, RIGHT), Tex("D", font_size = fs, color = RED).next_to(pD, RIGHT), Tex("E", font_size = fs, color = RED).next_to(pE, DL/2)
        line_ab, line_cd = Line(pA_coords, pB_coords, 0, color = BLUE), Line(pC_coords, pD_coords, 0, color = RED)
        
        self.play(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), FadeIn(pC), FadeIn(pC_label), FadeIn(pD), FadeIn(pD_label), Create(line_ab), Create(line_cd), run_time = 2)
        self.wait(2)
        arc = Arc(1, -PI, -PI, arc_center = pB_coords)
        trazar_arco(self, arc)
        line_ext = Line(pB_coords, [3.0, 0.0, 0.0], buff = DEFAULT_DOT_RADIUS, color = RED)
        self.play(AnimationGroup(Create(line_ext), FadeIn(pE), FadeIn(pE_label), FadeOut(arc), lag_ratio = 0.2, run_time = 1))
        self.wait(3)
        self.play(Uncreate(line_ab), Uncreate(line_cd), Uncreate(line_ext), FadeOut(pA), FadeOut(pA_label), FadeOut(pB), FadeOut(pB_label), FadeOut(pC), FadeOut(pC_label), FadeOut(pD), FadeOut(pD_label), FadeOut(pE), FadeOut(pE_label), run_time = 2)
        self.wait(3)