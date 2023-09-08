from manim import *
from numpy import *
from utils import *

fs = 48
# Sección 5.5
class manim_14_2(Scene):
    def construct(self):
        # Legend as left upper rectangle
        facts = Tex(r"Sabemos que:", font_size = fs, color = BLUE).to_corner(UL)
        bullet_1 = Tex(r"1) ", font_size = fs*0.75, color = BLUE).next_to(facts, LEFT + DOWN*1.5).shift([0.7, 0, 0])
        fact_1 = Tex(r"$e^{a}$ es trascendental $\forall a \neq 0$", font_size = fs*0.75, color = GRAY_B).next_to(bullet_1, RIGHT)
        bullet_2 = Tex(r"2) ", font_size = fs*0.75, color = BLUE).next_to(bullet_1, DOWN*1.5)
        fact_2 = Tex(r"$e^{i \pi}$ es trascendental", font_size = fs*0.75, color = GRAY_B).next_to(bullet_2, RIGHT).shift([0, 0.05, 0])

        v_line = Line([0, 4, 0], [0, 1.1, 0]).shift([-1, 0, 0]).set_color(BLUE)
        h_line = Line([-11, 1.1, 0], [-1, 1.1, 0]).set_color(BLUE)

        self.play(Write(facts))
        self.play(Write(bullet_1), Write(fact_1))
        self.play(Write(bullet_2), Write(fact_2))
        self.play(Create(v_line), Create(h_line))
        self.wait()

        # Proof by contradiction
        goal = Tex(r"¿Es $\pi$ algebraico?", font_size = fs * 1.2, color = ORANGE).to_edge(UP).shift([3, 0, 0])
        sup_1 = Tex(r"Supongamos ", font_size = fs * 1.2, color = ORANGE)
        sup_2 = Tex(r"que ", font_size = fs * 1.2).next_to(sup_1, RIGHT).shift([0, -0.05, 0])
        sup_3 = Tex(r"SÍ", font_size = fs * 1.2, color = ORANGE).next_to(sup_2, RIGHT).shift([0, 0.1, 0])
        sup = VGroup(sup_1, sup_2, sup_3).align_to(goal, DOWN + LEFT).shift([-0.5, -1, 0])

        self.play(Write(goal))
        self.play(Write(sup))
        self.wait()

        imply = Tex(r"$\Longrightarrow$", font_size = fs * 2.25).rotate(-PI/2 - PI/4).next_to(sup, DOWN)
        pol_1 = MathTex(r"\exists\, f(z) = a_nz^n + a_{n-1}z^{n-1} + ... + a_1z + a_0", font_size = fs)
        pol_2_1 = MathTex(r"\text{con }", font_size = fs).next_to(pol_1, DOWN)
        pol_2_2 = MathTex(r"a_i \in \mathbb{Q}", font_size = fs).next_to(pol_2_1, RIGHT)
        pol_2_3 = MathTex(r",\, a_n \neq 0").next_to(pol_2_2, RIGHT)
        pol_2 = VGroup(pol_2_1, pol_2_2, pol_2_3)
        pol_3 = MathTex(r"\text{tal que } f(e^{i \pi}) = 0", font_size = fs).next_to(pol_2, DOWN)

        self.play(Write(imply))
        self.play(Write(pol_1))
        self.play(Write(pol_2))
        self.play(Write(pol_3))
        self.wait()

        pol = VGroup(pol_1, pol_2, pol_3)
        sups = Tex(r"Suponemos que:", font_size = fs, color = ORANGE).shift([-5, 0.5, 0])
        v_line_2 = Line([0, 1.1, 0], [0, -1.8, 0]).shift([-1, 0, 0]).set_color(ORANGE)
        h_line_2 = Line([-11, -1.8, 0], [-1, -1.8, 0]).set_color(ORANGE)
        self.play(Transform(sup, sups))
        self.play(pol.animate.scale(0.6))
        self.play(pol.animate.shift([-3.9, 0.1, 0]))
        self.play(
                  Create(h_line_2),
                  Create(v_line_2),
                  FadeOut(goal),
                  FadeOut(imply)
        )
        self.wait()

        g = Tex(r"g(x) := f(ix)\,f(-ix)", font_size = fs*1.3).to_edge(UP).shift([3, 0, 0])
        self.play(Write(g))

        g_real = Tex(r"g tiene coeficientes reales:", font_size = fs).next_to(g, DOWN * 2)
        g_real_proof_1_1 = MathTex(r"\overline{g(x)} =")
        g_real_proof_1_2 = MathTex(r"\overline{f(ix)f(-ix)}").next_to(g_real_proof_1_1, RIGHT)
        g_real_proof_1 = VGroup(g_real_proof_1_1, g_real_proof_1_2).next_to(g_real, DOWN)
        g_real_proof_2 = MathTex(r"= \overline{f(ix)}\;\overline{f(-ix)} = f(\overline{ix})f(\overline{-ix})").next_to(g_real_proof_1, DOWN)
        g_real_proof_3_1 = MathTex(r"= f(-ix)f(ix) =").next_to(g_real_proof_2, DOWN)
        g_real_proof_3_2 = MathTex(r"g(x)").next_to(g_real_proof_3_1, RIGHT)
        g_real_proof_3 = VGroup(g_real_proof_3_1, g_real_proof_3_2)

        self.play(Write(g_real))
        self.play(Write(g_real_proof_1), run_time=2)
        self.play(Write(g_real_proof_2), run_time=2)
        self.play(Write(g_real_proof_3), run_time=2)
        self.wait()
        self.play(AnimationGroup(
            FadeOut(g_real_proof_1_2),
            FadeOut(g_real_proof_2),
            FadeOut(g_real_proof_3_1),
            g_real_proof_3_2.animate.next_to(g_real_proof_1_1, RIGHT)
        ))
        self.wait()

        f_racional = Tex(r"f tiene coeficientes racionales", font_size = fs).next_to(g_real_proof_3, DOWN)
        self.play(Write(f_racional),
                ApplyWave(pol_2_2),
                pol_2_2.animate.set_color(ORANGE))
        self.wait()

        