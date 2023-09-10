from manim import *
from numpy import *
from utils import trazar_arco

aux_thick, aux_arc_len = DEFAULT_STROKE_WIDTH * 0.6, PI/16
fs = 40

# Sección 4.3
class manim_05_interr(Scene):
    def construct(self):
        # compilar con --save-sections para generar vídeos separados para cada sección
        # puntos base
        pA_coords, pB_coords, pC_coords, pD_coords = [-2.0, -2.0, 0.0], [2.0, 2.0, 0.0], [-2.0, 0.0, 0.0], [2.0, 0.0, 0.0]
        pA = Dot(pA_coords, color = RED)
        pA_label = Tex("$A = (-2, -2)$", font_size = fs*0.75, color = RED).next_to(pA, DOWN)
        pB = Dot(pB_coords, color = RED)
        pB_label = Tex("$B = (2, 2)$", font_size = fs*0.75, color = RED).next_to(pB, UP)
        pC = Dot(pC_coords, color = BLUE)
        pC_label = Tex("$C = (-2, 0)$", font_size = fs*0.75, color = BLUE).next_to(pC, DOWN)
        pD = Dot(pD_coords, color = BLUE)
        pD_label = Tex("$D = (2, 0)$", font_size = fs*0.75, color = BLUE).next_to(pD, DOWN)

        pA_interr = Tex("$A = (?, ?)$", font_size = fs*0.75, color = pA_label.get_color()).next_to(pA, DOWN)
        pB_interr = Tex("$B = (?, ?)$", font_size = fs*0.75, color = pB_label.get_color()).next_to(pB, UP)
        pC_interr = Tex("$C = (?, ?)$", font_size = fs*0.75, color = pC_label.get_color()).next_to(pC, DOWN)
        pD_interr = Tex("$D = (?, ?)$", font_size = fs*0.75, color = pD_label.get_color()).next_to(pD, DOWN)

        # puntos de interseccion
        pF = Dot([sqrt(7)-1, sqrt(7)-1, 0.0], color = WHITE)
        pF_label = Tex("F", font_size = fs).next_to(pF, RIGHT)

        # lineas y rectas
        line = Line(pA_coords, pB_coords, color = RED, buff = DEFAULT_DOT_RADIUS)
        circle = Arc(arc_center = pC_coords, start_angle = -PI/4, angle = PI/2, radius = 4, stroke_color = BLUE)
        
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pB), FadeIn(pA_label), FadeIn(pB_label), FadeIn(pC), FadeIn(pD), FadeIn(pC_label), FadeIn(pD_label), lag_ratio = 0.5))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        trazar_arco(self, circle)
        self.wait(1)
        self.play(FadeIn(pF), FadeIn(pF_label))
        self.wait(1)
        self.play(AnimationGroup(Transform(pA_label, pA_interr),  Transform(pC_label, pC_interr), Transform(pD_label, pD_interr), Transform(pB_label, pB_interr),  lag_ratio = 1.0, run_time = 3.0))
        self.wait(2)
        self.play(Indicate(pA_label, color = RED_E), Indicate(pB_label, color = RED_E),Indicate(pC_label, color = BLUE_E), Indicate(pD_label, color = BLUE_E), run_time = 2.0)
        self.wait(3)