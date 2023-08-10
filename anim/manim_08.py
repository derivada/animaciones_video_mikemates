from manim import *
from numpy import *
from utils import *

fs = 36
color_A, color_B, color_AB = BLUE, RED, PURPLE

# Sección 4.6
class manim_08(Scene):
    def construct(self):        
        # puntos A y B
        # angulo = 45º, A = 3, B = 2, base_len = 2
        mostrar_grid(self)
        pA_coords, pB_coords, pAB_coords, p1_coords = [3.0, 0.0, 0.0], [sqrt(2), sqrt(2), 0.0], [6.0, 0.0, 0.0], [sqrt(2)/2, sqrt(2)/2, 0.0]
        p0, p1, pA, pB, pAB = Dot(ORIGIN), Dot(p1_coords), Dot(pA_coords, color = color_A), Dot(pB_coords, color = color_B), Dot(pAB_coords, color = color_AB)
        self.add(p0)
        pA_label = Tex("A", color = color_A, font_size = fs).next_to(pA, DR/2)
        pB_label = Tex("B", color = color_B, font_size = fs).next_to(pB, DR/2)
        pAB_label = Tex("AB", color = color_AB, font_size = fs).next_to(pAB, DR/2)
        line_a = Line(ORIGIN, pA_coords, DEFAULT_DOT_RADIUS, color = color_A)
        line_b = Line(ORIGIN, pB_coords, DEFAULT_DOT_RADIUS, color = color_B)
        line_1a = Line(p1_coords, pA_coords, DEFAULT_DOT_RADIUS, stroke_width = DEFAULT_STROKE_WIDTH * 0.66, color = LIGHT_GRAY)
        line_bab = Line(pB_coords, pAB_coords, DEFAULT_DOT_RADIUS, stroke_width = DEFAULT_STROKE_WIDTH * 0.66, color = color_AB)
        proportion_eq = Tex(r"$\frac{1}{b} = \frac{a}{ab}$", font_size = fs*1.5).next_to(line_bab, UP)

        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), Create(line_a), Create(line_b), lag_rate = 0.2, run_time = 2))

        arc_1 = Arc(1, 0, PI/4, color = LIGHT_GRAY)
        trazar_arco(self, arc_1)
        self.play(FadeIn(p1))
        self.play(Create(line_1a))
        self.wait(2)
        
        self.play(Create(line_bab))
        self.play(FadeIn(pAB))
        self.wait(2)

        self.play(DrawBorderThenFill(proportion_eq), run_time = 2)
        self.wait(2)

        self.play(FadeIn(pAB_label))
        self.play(Indicate(pAB), Indicate(pAB_label))
        self.wait(3)