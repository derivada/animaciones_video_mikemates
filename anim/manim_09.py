from manim import *
from numpy import *
from utils import *

fs = 30
color_A, color_B, color_sqrtA = BLUE, PURPLE, MAROON

# Sección 4.7
class manim_09(Scene):
    def construct(self):        
        # puntos A = 3, B = -1, C = sqrt(3)
        mostrar_grid(self)
        pA_coords, pB_coords, pmid_coords, psqrtA_coords = [3.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, sqrt(3), 0.0]
        p0, pA, pB, psqrtA = Dot(ORIGIN), Dot(pA_coords, color = color_A), Dot(pB_coords, color = color_B), Dot(psqrtA_coords, color = color_sqrtA)
        p0_label = Tex("O", color = LIGHT_GRAY, font_size = fs).next_to(p0, DL/2)
        self.play(FadeIn(p0), FadeIn(p0_label))
        pA_label = Tex("A", color = color_A, font_size = fs).next_to(pA, DL/2)
        pB_label = Tex("B", color = color_B, font_size = fs).next_to(pB, DL/2)
        psqrtA_label = Tex("C", color = color_sqrtA, font_size = fs).next_to(psqrtA_coords, LEFT) # nombre temporal C, se cambia luego
        line_a = Line(ORIGIN, pA_coords, DEFAULT_DOT_RADIUS, color = color_A)
        line_b = Line(ORIGIN, pB_coords, DEFAULT_DOT_RADIUS, color = color_B)
        line_sqrta = Line(ORIGIN, psqrtA_coords, DEFAULT_DOT_RADIUS, color = color_sqrtA)
        arc = Arc(2, 0, PI, arc_center = pmid_coords, color = LIGHT_GRAY, stroke_width = DEFAULT_STROKE_WIDTH*0.66)
        triangle_obc = Polygram([ORIGIN, pB_coords, psqrtA_coords], color = LIGHT_GRAY)
        similar = Tex(r"$\triangle ABC \sim \triangle OBC$", font_size = fs * 1.5).move_to([-4.0, 3.0, 0.0])
        proportion_eq1 = Tex(r"$\frac{OB}{OC} = \frac{OC}{OA}$", font_size = fs * 1.5).next_to(similar, DOWN).align_to(similar, LEFT)
        proportion_eq2 = Tex(r"$OC^2 = OA \cdot OB$", font_size = fs * 1.5).next_to(proportion_eq1, DOWN).align_to(proportion_eq1, LEFT)
        proportion_eq3 = Tex(r"$OC = \sqrt{OA \cdot OB} = \sqrt{OA \cdot 1}$", font_size = fs * 1.5).move_to([-3.5, -1.3, 0])

        result = Tex(r"$OC = \sqrt{OA}$", color = color_sqrtA, font_size = fs * 1.5).next_to(proportion_eq3, DOWN).align_to(proportion_eq3, LEFT)

        measure_sqrt_a = Tex("OC = ?", color = color_sqrtA, font_size = fs * 1.5).to_corner(DR)
        measure_b = Tex("OB = 1", color = color_B, font_size = fs * 1.5).next_to(measure_sqrt_a, UP)
        measure_a = Tex("OA = 3", color = color_A, font_size = fs * 1.5).next_to(measure_b, UP)

        # setup puntos
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), Create(line_a), lag_rate = 0.2, run_time = 1.5))
        self.play(Write(measure_a), run_time=0.5)
        self.wait(1)
        self.play(AnimationGroup(FadeIn(pB), FadeIn(pB_label), Create(line_b), lag_rate = 0.2, run_time = 1.5))
        self.play(Write(measure_b), run_time=0.5)
        self.wait(2)

        # semicircunf.
        trazar_arco(self, arc, show_vect = False)
        self.wait(2)

        # linea hasta C (sqrtA)
        self.play(AnimationGroup(Create(line_sqrta), FadeIn(psqrtA), FadeIn(psqrtA_label),  lag_ratio = 0.2, run_time = 2))
        self.play(Write(measure_sqrt_a), run_time=0.5)
        self.wait(1.5)
        
        # triangulo proporcional
        self.play(Create(triangle_obc))
        self.play(Transform(triangle_obc, Polygram([ORIGIN, psqrtA_coords, pA_coords], color = LIGHT_GRAY)), run_time = 2)
        self.wait(1)

        # ecuaciones proporcionalidad
        self.play(DrawBorderThenFill(similar), run_time = 2)
        self.wait()
        self.play(DrawBorderThenFill(proportion_eq1), FadeOut(triangle_obc), run_time = 1)
        self.wait()
        self.play(DrawBorderThenFill(proportion_eq2), run_time = 1)
        self.wait()
        self.play(DrawBorderThenFill(proportion_eq3), run_time = 1)
        self.wait()
        self.play(Write(result), run_time = 2)
        self.wait()

        # done
        self.play(Transform(psqrtA_label, Tex(r"$\sqrt{3}$", color = color_sqrtA, font_size = fs * 1.5).next_to(psqrtA_coords, UL)), 
                  Transform(measure_sqrt_a, Tex(r"OC $= \sqrt{3}$", color = color_sqrtA, font_size = fs * 1.5).to_corner(DR)),
                  run_time = 2)
        self.play(Indicate(psqrtA_label))
        self.wait(6)