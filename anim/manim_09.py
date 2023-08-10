from manim import *
from numpy import *
from utils import *

fs = 28
color_A, color_B, color_sqrtA = BLUE, LIGHT_GRAY, BLUE_B

# Sección 4.7
class manim_09(Scene):
    def construct(self):        
        # puntos A = 3, B = -1, C = sqrt(3)
        mostrar_grid(self)
        pA_coords, pB_coords, pmid_coords, psqrtA_coords = [3.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, sqrt(3), 0.0]
        p0, pA, pB, psqrtA = Dot(ORIGIN), Dot(pA_coords, color = color_A), Dot(pB_coords, color = color_B), Dot(psqrtA_coords, color = color_sqrtA)
        p0_label = Tex("O", color = LIGHT_GRAY, font_size = fs).next_to(p0, DL/2)
        self.add(p0, p0_label)
        pA_label = Tex("A", color = color_A, font_size = fs).next_to(pA, DL/2)
        pB_label = Tex("B", color = color_B, font_size = fs).next_to(pB, DL/2)
        psqrtA_label = Tex("C", color = color_sqrtA, font_size = fs).next_to(psqrtA_coords, LEFT) # nombre temporal C, se cambia luego
        line_a = Line(ORIGIN, pA_coords, DEFAULT_DOT_RADIUS, color = color_A)
        line_b = Line(ORIGIN, pB_coords, DEFAULT_DOT_RADIUS, color = color_A)
        line_sqrta = Line(ORIGIN, psqrtA_coords, DEFAULT_DOT_RADIUS, color = color_sqrtA)
        arc = Arc(2, 0, PI, arc_center = pmid_coords, color = LIGHT_GRAY, stroke_width = DEFAULT_STROKE_WIDTH*0.66)
        triangle_obc = Polygram([ORIGIN, pB_coords, psqrtA_coords], color = LIGHT_GRAY)
        proportion_eq1 = Tex(r"$\frac{OB}{OC} = \frac{OC}{OA}$", font_size = fs).move_to([-4.0, 3.0, 0.0])
        proportion_eq2 = Tex(r"$OC^2 = OA \cdot OB = 3 \cdot 1 = 3$", font_size = fs).next_to(proportion_eq1, DOWN).align_to(proportion_eq1, LEFT)
        proportion_eq3 = Tex(r"$OC = \sqrt{3}$", font_size = fs, color = color_sqrtA).next_to(proportion_eq2, DOWN).align_to(proportion_eq2, LEFT)

        # setup puntos
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), Create(line_a), lag_rate = 0.2, run_time = 2))
        self.wait(1)
        self.play(AnimationGroup(FadeIn(pB), FadeIn(pB_label), Create(line_b), lag_rate = 0.2, run_time = 2))
        self.wait(2)

        # semicircunf.
        trazar_arco(self, arc, show_vect = False)
        self.wait(2)

        # linea hasta C (sqrtA)
        self.play(AnimationGroup(Create(line_sqrta), FadeIn(psqrtA), FadeIn(psqrtA_label), lag_ratio = 0.2, run_time = 2))
        self.wait(2)
        
        # triangulo proporcional
        self.play(Create(triangle_obc))
        self.play(Transform(triangle_obc, Polygram([ORIGIN, psqrtA_coords, pA_coords], color = LIGHT_GRAY)), run_time = 2)
        self.wait(1)

        # ecuaciones proporcionalidad
        self.play(DrawBorderThenFill(proportion_eq1), FadeOut(triangle_obc), run_time = 2)
        self.wait(2)
        self.play(DrawBorderThenFill(proportion_eq2), run_time = 2)
        self.wait(2)
        self.play(DrawBorderThenFill(proportion_eq3), run_time = 2)
        self.wait(2)

        # done
        self.play(Transform(psqrtA_label, Tex(r"$\sqrt{3}$", color = color_B, font_size = fs).next_to(psqrtA_coords, LEFT)), run_time = 2)
        self.play(Indicate(psqrtA_label))
        self.wait(3)