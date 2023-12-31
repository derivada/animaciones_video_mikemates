from manim import *
from numpy import *
from utils import *

fs = 48
# Sección 5.5
class manim_14(Scene):
    def construct(self):
        # primera parte: descubrir que e^i*pi es transcendental
        eq_pos, lista_pos = [0.0, 2.25, 0.0], [-3.0, 2.5, 0.0]
        euler_eq = Tex(r"$e^{i \pi} + 1 = 0$", font_size = fs*1.5, color = GRAY_B).shift(eq_pos)
        self.play(DrawBorderThenFill(euler_eq))
        self.wait(3)

        pentagon = RegularPolygon(5).scale(2).shift([0, -1, 0])
        verts_pent = pentagon.get_vertices()
        i = Tex(r"$i = \sqrt{-1}$", font_size = fs, color = RED).scale(1.2).move_to(verts_pent[0])
        pi = Tex(r"$\pi$", font_size = fs, color = YELLOW).scale(1.2).move_to(verts_pent[1])
        e = Tex(r"$e$", font_size = fs, color = GREEN).scale(1.2).next_to(pi, RIGHT).move_to(verts_pent[2])
        n_1 = Tex(r"$1$", font_size = fs, color = BLUE).scale(1.2).next_to(e, RIGHT).move_to(verts_pent[4])
        n_0 = Tex(r"$0$", font_size = fs, color = PURPLE).scale(1.2).next_to(n_1, RIGHT).move_to(verts_pent[3])
        self.play(FadeIn(e))
        self.play(FadeIn(pi))
        self.play(FadeIn(i))
        self.play(FadeIn(n_1))
        self.play(FadeIn(n_0))
        self.wait()

        #group = VGroup(e, pi, i, n_1, n_0)
        self.play(AnimationGroup(FadeOut(e), FadeOut(pi), FadeOut(i), FadeOut(n_1), FadeOut(n_0), lag_ratio = 0.2, run_time = 2))
        #self.play(ShrinkToCenter(group))
        self.wait()

        poly_eq = MathTex(r"z + 1 = 0", font_size = fs*1.5, color = GRAY_B).shift(eq_pos)
        poly_root_1 = Tex(r"$e^{i \pi}$", font_size = fs * 1.5)
        poly_root_2 = Tex(" es solución", font_size = fs* 1.5)
        poly_root = VGroup(poly_root_1, poly_root_2).arrange().next_to(poly_eq, DOWN * 3)
        imply = Tex(r"$\Longrightarrow$", font_size = fs * 1.5).rotate(-PI/2).next_to(poly_root, DOWN)
        e_alg = Tex(r"$e^{i \pi}$ es algebraico", font_size = fs * 1.5).next_to(imply, DOWN * 2)
        self.play(AnimationGroup(
            FadeOut(euler_eq, shift=UP*1.5),
            FadeIn(poly_eq, shift=UP*1.5),
        ))
        self.play(FadeIn(poly_root), run_time = 2)
        self.play(Write(imply))
        self.play(FadeIn(e_alg))
        self.play(e_alg.animate.set_color(YELLOW))
        self.play(ApplyWave(e_alg))
        self.wait()
        self.play(AnimationGroup(
            FadeOut(poly_eq),
            FadeOut(poly_root),
            FadeOut(imply),
            FadeOut(e_alg)
        ))




"""
        poly_eq = Tex(r"$z - 1 = 0$", font_size = fs*1.5, color = GRAY_B).shift(eq_pos)
        poly_root_1 = Tex(r"Tiene a", font_size = fs)
        poly_root_2 = Tex(r"$e^{i \pi}$", font_size = fs, color = BLUE)
        poly_root_3 = Tex(r"como raíz", font_size = fs)
        poly_root_line = VGroup(poly_root_1, poly_root_2, poly_root_3).arrange().next_to(poly_eq, DOWN)
        alg_1 = Tex(r"$e^{i \pi}$", font_size = fs, color = BLUE)
        alg_2 = Tex(r"es algebraico", font_size = fs)
        arrow = Tex(r"$\Longrightarrow$", font_size = fs).rotate(-PI/2).next_to(poly_root_line, DOWN)
        alg_line = VGroup(alg_1, alg_2).arrange().next_to(arrow, DOWN)
        self.play(Transform(euler_eq, poly_eq), FadeIn(poly_root_line), run_time = 2)
        self.wait(3)
        self.play(DrawBorderThenFill(arrow), FadeIn(alg_line), run_time = 2)
        self.wait(3)
        self.play(AnimationGroup(FadeOut(euler_eq), FadeOut(poly_eq), FadeOut(poly_root_line), FadeOut(arrow), alg_line.animate.shift(lista_pos), lag_ratio = 0.2, run_time = 2))
        
        sup = Tex("Supongamos que $\pi$ el algebraico, raíz de algún $f(x)$", font_size = fs).next_to(alg_line, DOWN*1.5).align_to(alg_line, LEFT).shift(LEFT)
        deducc_1 = Tex("Definimos: $g(x) = f(ix)f(-ix)$. Tenemos que:", font_size = fs).next_to(sup, DOWN*1.5).align_to(sup, LEFT)
        deducc_2 = Tex("$\overline{g(x)} = \overline{f(ix)f(-ix)} = \overline{f(ix)}\;\overline{f(-ix)} = f(\overline{ix})f(\overline{-ix}) = f(-ix)f(ix)=g(x)$", font_size = fs*0.75).next_to(deducc_1, DOWN).align_to(deducc_1, LEFT)
        res_2 = Tex("Por lo tanto $g(x)$ tiene coeficientes reales (y racionales). Además:", font_size = fs).next_to(deducc_2, DOWN).align_to(deducc_2, LEFT)
        deducc_3 = Tex("$g(i\pi) = f(i^2\pi)f(-i^2\pi) = f(-(\sqrt{-1})^2\pi)f(-(\sqrt{-1})^2\pi)= f(-\pi)f(\pi)=0$", font_size = fs*0.75).next_to(deducc_2, DOWN).align_to(deducc_2, LEFT)
        res = Tex("Por lo tanto $i\pi$ es raíz de $g(x) \Longrightarrow i\pi$ es algebraico").next_to(deducc_3, DOWN).align_to(deducc_3, LEFT)

        self.play(DrawBorderThenFill(sup), run_time = 2)
        self.wait(2)
        self.play(FadeIn(deducc_1))
        self.wait(2)
        self.play(DrawBorderThenFill(res_2), run_time = 2)
        self.wait(2)
        self.play(FadeIn(deducc_2))
        self.wait(2)        
        self.play(FadeIn(deducc_3))
        self.wait(2)
        self.play(DrawBorderThenFill(res), run_time = 2)
        self.wait(3)
        """