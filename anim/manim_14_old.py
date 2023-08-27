from manim import *
from numpy import *
from utils import *

fs = 48
# Sección 5.5
class manim_14(Scene):
    def construct(self):
        # primera parte: descubrir que e^i*pi es transcendental
        eq_pos, lista_pos = [0.0, 2.5, 0.0], [-3.0, 2.5, 0.0]
        euler_eq = Tex(r"$e^{i \pi} - 1 = 0$", font_size = fs*1.5, color = GRAY_B).shift(eq_pos)
        self.play(DrawBorderThenFill(euler_eq))
        self.wait(3)
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
        
        # lista de resultados necesarios para la prueba
        lista_1 = Tex("1.", font_size = fs, color = GRAY_B).next_to(alg_line, LEFT)
        self.play(FadeIn(lista_1), run_time = 0.5)
        self.wait(3)
        lista_2 = Tex("2.", font_size = fs, color = GRAY_B).next_to(lista_1, DOWN*1.5)
        i_alg_1 = Tex(r"$i = \sqrt{-1}$ ", color = BLUE, font_size = fs).next_to(lista_2, RIGHT)
        i_alg_2 = Tex(r"es algebraico por ser raíz de $x^2 + 1 = 0$", font_size = fs).next_to(i_alg_1, RIGHT)
        i_alg_line = VGroup(i_alg_1, i_alg_2)
        self.play(FadeIn(i_alg_line), FadeIn(lista_2), run_time = 2)
        self.wait(3)
        lista_3 = Tex("3.", font_size = fs, color = GRAY_B).next_to(lista_2, DOWN*1.5)
        prod_alg_1 = Tex(r"El ", font_size = fs).next_to(lista_3, RIGHT)
        prod_alg_2 = Tex(r"producto de algebraicos ", color = BLUE, font_size = fs).next_to(prod_alg_1, RIGHT)
        prod_alg_3 = Tex(r"es algebraico", font_size = fs).next_to(prod_alg_2, RIGHT)
        prod_alg_line = VGroup(prod_alg_1, prod_alg_2, prod_alg_3)
        self.play(FadeIn(prod_alg_line), FadeIn(lista_3), run_time = 2)
        self.wait(3)
        lista_4 = Tex("4.", font_size = fs, color = GRAY_B).next_to(lista_3, DOWN*1.5)
        ea_trans_1 = Tex(r"$e^a$ ", color = BLUE, font_size = fs).next_to(lista_4, RIGHT)
        ea_trans_2 = Tex("es transcendental si $a$ es algebraico", font_size = fs).next_to(ea_trans_1, RIGHT)
        ea_trans_line = VGroup(ea_trans_1, ea_trans_2)
        self.play(FadeIn(ea_trans_line), FadeIn(lista_4), run_time = 2)
        self.wait(3)

        # prueba por contradicción
        sup_1 = Tex(r"Supongamos que $\pi$ es", font_size = fs).next_to(ea_trans_line, DOWN*2).shift(LEFT)
        sup_2 = Tex(r"algebraico", font_size = fs, color = BLUE).next_to(sup_1, RIGHT)
        sup_3 = Tex(r"$\Longrightarrow$").next_to(sup_2, RIGHT)
        sup_line = VGroup(sup_1, sup_2, sup_3)
        step1 = Tex(r"$i \cdot \pi$ es algebraico $\Longrightarrow$", font_size = fs).next_to(sup_line, DOWN).align_to(sup_line, LEFT)
        step2 = Tex(r"$e^{i \pi}$ es transcendental", font_size = fs).next_to(step1, DOWN).align_to(step1, LEFT)
        contr = Tex(r"Contradicción!", color = RED, font_size = fs).next_to(step2, DOWN).align_to(step2, RIGHT)
        self.play(DrawBorderThenFill(sup_line), run_time = 2)
        self.wait(2)
        self.play(DrawBorderThenFill(step1), run_time = 2)
        self.wait(2)        
        self.play(DrawBorderThenFill(step2), run_time = 2)
        self.wait(2)
        self.play(Indicate(lista_1, color = RED, scale_factor = 1.1), Indicate(alg_line, color = RED, scale_factor = 1.1), Indicate(step2, color = RED, scale_factor = 1.1), run_time = 3)
        self.wait(2)
        self.play(FadeIn(contr))
        self.wait(3)
        
        cross = Line(sup_2.get_boundary_point(LEFT) + LEFT/6 + UP/25 , sup_2.get_boundary_point(RIGHT) + RIGHT/6 + UP/25, buff = 0, color = BLUE)
        self.play(Create(cross))

        # clear scene
        self.play(AnimationGroup(*[FadeOut(mobj) for mobj in self.mobjects]), lag_ratio = 0.1, run_time = 2)

        # final: pi es transcendental
        pi_trans = Tex(r"$\pi$ es transcendental", font_size = 72)
        self.play(DrawBorderThenFill(pi_trans), run_time = 2)
        self.play(ShowPassingFlash(Underline(pi_trans, color = BLUE)))

        self.wait(3)