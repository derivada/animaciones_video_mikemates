from manim import *
from numpy import *
from utils import *

fs = 36
color_A, color_B, color_AB = BLUE, RED, PURPLE

# Sección 4.6
class manim_08(Scene):
    def construct(self):        
        # puntos A y B
        # angulo = 45º, A = 3, B = 2
        mostrar_grid(self)
        pA_coords, pB_coords, pAB_coords, p1_coords = [3.0, 0.0, 0.0], [sqrt(2), sqrt(2), 0.0], [6.0, 0.0, 0.0], [sqrt(2)/2, sqrt(2)/2, 0.0]
        p0, p1, pA, pB, pAB = Dot(ORIGIN), Dot(p1_coords), Dot(pA_coords, color = color_A), Dot(pB_coords, color = color_B), Dot(pAB_coords, color = color_AB)
        self.play(FadeIn(p0))
        line_a = Line(ORIGIN, pA_coords, DEFAULT_DOT_RADIUS, color = color_A)
        line_b = Line(ORIGIN, pB_coords, DEFAULT_DOT_RADIUS, color = color_B)
        line_1a = Line(p1_coords, pA_coords, DEFAULT_DOT_RADIUS, stroke_width = DEFAULT_STROKE_WIDTH * 0.66, color = LIGHT_GRAY)
        line_bab = Line(pB_coords, pAB_coords, DEFAULT_DOT_RADIUS, stroke_width = DEFAULT_STROKE_WIDTH * 0.66, color = LIGHT_GRAY)
        line_ab = Line(pA_coords, pAB_coords, DEFAULT_DOT_RADIUS, color = color_AB)
        line_origin_ab = Line(ORIGIN, pAB_coords, DEFAULT_DOT_RADIUS, color = color_AB)
        p1_label = Tex("1", color = WHITE, font_size = fs).next_to(p1, UP).shift(DOWN * 0.2 + LEFT * 0.2)
        pA_label = Tex("A", color = color_A, font_size = fs * 1.2).next_to(line_a, DOWN * 1.2)
        pB_label = Tex("B", color = color_B, font_size = fs * 1.2).next_to(line_b, LEFT).shift(UP * 0.8 + RIGHT * 1.3)
        pAB_label = Tex("AB", color = color_AB, font_size = fs * 1.2).next_to(line_bab, DOWN * 1.2)
        proportion_eq = Tex(r"$\frac{1}{B} = \frac{A}{AB}$", font_size = fs*2).next_to(line_bab, UP*2)

        measure_ab = Tex("AB = 6", color = color_AB, font_size = fs).to_corner(DR)
        measure_b = Tex("B = 2", color = color_B, font_size = fs).next_to(measure_ab, UP)
        measure_a = Tex("A = 3", color = color_A, font_size = fs).next_to(measure_b, UP)
        proportion_real = Tex(r"$\frac{1}{2} = \frac{3}{6}$", font_size = fs*2).next_to(measure_b, LEFT * 4)

        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), Create(line_a), Create(line_b), lag_rate = 0.2, run_time = 1.5))
        self.play(Write(measure_a), Write(measure_b), run_time=0.5)

        arc_1 = Arc(1, 0, PI/4, color = LIGHT_GRAY)
        trazar_arco(self, arc_1)
        self.play(FadeIn(p1), Write(p1_label))
        self.play(Create(line_1a))
        self.wait(2)
        
        self.play(Create(line_bab), Create(line_ab))
        self.play(FadeIn(pAB))
        self.wait(2)

        self.play(DrawBorderThenFill(proportion_eq), run_time = 2)
        self.wait(2)

        self.play(FadeIn(pAB_label), Write(measure_ab))
        self.play(AnimationGroup(
            line_origin_ab.animate.set_color(YELLOW),
            AnimationGroup(Indicate(pAB), Indicate(pAB_label)),
            lag_ratio=0.2, run_time=0.8
        ))
        # Remove line_origin_ab
        self.remove(line_origin_ab)
        self.play(line_a.animate.set_color(color_A),
                   line_ab.animate.set_color(color_AB),
                   run_time=0.2)
        self.play(DrawBorderThenFill(proportion_real))
        self.wait()

        self.play(Uncreate(line_a), Uncreate(line_b), Uncreate(line_bab), Uncreate(line_1a), Uncreate(arc_1), Uncreate(line_ab))
        self.play(FadeOut(p0), FadeOut(p1), FadeOut(pA), FadeOut(pB), FadeOut(pAB), FadeOut(pA_label), FadeOut(pB_label), FadeOut(pAB_label), FadeOut(proportion_eq))