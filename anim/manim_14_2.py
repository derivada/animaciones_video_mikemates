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
        fact_1_text = Tex(r"$e^{a}$ es transcendental", font_size = fs*0.75, color = GRAY_B).next_to(bullet_1, RIGHT)
        fact_1_subtext = Tex(r"(a algebraico, $a \neq 0$)", color = GRAY_B, font_size = fs*0.5).next_to(fact_1_text, DOWN/4).shift(RIGHT/2)
        fact_1 = VGroup(fact_1_text, fact_1_subtext)
        bullet_2 = Tex(r"2) ", font_size = fs*0.75, color = BLUE).next_to(bullet_1, DOWN*1.5)
        fact_2 = Tex(r"$e^{i \pi}$ es algebraico", font_size = fs*0.75, color = GRAY_B).next_to(bullet_2, RIGHT).shift([0, 0.05, 0])

        # Lines of the rectangle
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
        sup_3 = Tex(r"SÍ", font_size = fs * 1.2, color = ORANGE).next_to(sup_2, RIGHT).align_to(sup_2, DOWN)
        sup = VGroup(sup_1, sup_2, sup_3).align_to(goal, DOWN + LEFT).shift([-0.5, -1, 0])

        self.play(Write(goal))
        self.play(Write(sup))
        self.wait()

        # Suppositions
        imply = Tex(r"$\Longrightarrow$", font_size = fs * 2.25).rotate(-PI/2 - PI/4).next_to(sup, DOWN)
        pol_1 = MathTex(r"\exists\, f(z) = a_nz^n + a_{n-1}z^{n-1} + ... + a_1z + a_0", font_size = fs)
        pol_2_1 = MathTex(r"\text{con }", font_size = fs).next_to(pol_1, DOWN)
        pol_2_2 = MathTex(r"a_i \in \mathbb{Q}", font_size = fs).next_to(pol_2_1, RIGHT)
        pol_2_3 = MathTex(r",\, a_n \neq 0").next_to(pol_2_2, RIGHT)
        pol_2 = VGroup(pol_2_1, pol_2_2, pol_2_3)
        pol_3 = MathTex(r"\text{tal que } f(\pi) = 0", font_size = fs).next_to(pol_2, DOWN)
        sup_group = VGroup(pol_1, pol_2, pol_3)
        self.play(Write(imply))
        self.play(Write(pol_1))
        self.play(Write(pol_2))
        self.play(Write(pol_3))
        self.wait()

        # Move suppositions to legend
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

        # Introduce g
        g = Tex(r"g(x) := f(ix)\,f(-ix)", font_size = fs*1.3).to_edge(UP).shift([3, 0, 0])
        self.play(Write(g))

        # g has real coefficients
        g_real = Tex(r"g tiene coeficientes reales", font_size = fs).next_to(g, DOWN * 2)
        g_real_proof_1_1 = MathTex(r"\overline{g(x)} =")
        g_real_proof_1_2 = MathTex(r"\overline{f(ix)f(-ix)}").next_to(g_real_proof_1_1, RIGHT)
        g_real_proof_1 = VGroup(g_real_proof_1_1, g_real_proof_1_2).next_to(g_real, DOWN)
        g_real_proof_2 = MathTex(r"= \overline{f(ix)}\;\overline{f(-ix)} = f(\overline{ix})f(\overline{-ix})").next_to(g_real_proof_1, DOWN)
        g_real_proof_3_1 = MathTex(r"= f(-ix)f(ix) =").next_to(g_real_proof_2, DOWN)
        g_real_proof_3_2 = MathTex(r"g(x)").next_to(g_real_proof_3_1, RIGHT)
        g_real_proof_3 = VGroup(g_real_proof_3_1, g_real_proof_3_2)

        self.play(Write(g_real))
        self.play(Write(g_real_proof_1), run_time=2)
        self.play(Write(g_real_proof_2), run_time=3)
        self.play(Write(g_real_proof_3), run_time=2)
        self.wait()
        self.play(AnimationGroup(
            FadeOut(g_real_proof_1_2),
            FadeOut(g_real_proof_2),
            FadeOut(g_real_proof_3_1),
            g_real_proof_3_2.animate.next_to(g_real_proof_1_1, RIGHT)
        ))
        self.wait()

        # g has rational coefficients
        f_rational = Tex(r"f tiene coeficientes racionales", font_size = fs).next_to(g_real, DOWN)
        statements = VGroup(g_real, f_rational)
        brace = Brace(Line(LEFT * 0.6, RIGHT * 0.6)).rotate(PI/2).next_to(statements, RIGHT)
        imply = Tex(r"$\Longrightarrow$", font_size = fs).next_to(statements, DOWN + LEFT).shift([0.5, -0.4, 0])
        g_rational = Tex(r"g tiene coeficientes racionales", font_size = fs, color=ORANGE).next_to(imply, RIGHT)
        self.play(FadeOut(g_real_proof_1_1),
                  FadeOut(g_real_proof_3_2))
        self.play(Write(f_rational),
                ApplyWave(pol_2_2),
                pol_2_2.animate.set_color(ORANGE))
        self.play(pol_2_2.animate.set_color(WHITE),
            Write(brace), Write(imply), Write(g_rational))
        self.wait(2)

        self.play(FadeOut(g_real), FadeOut(f_rational), FadeOut(brace), FadeOut(imply))
        self.play(g_rational.animate.shift([-0.5, 1.5, 0]))
        self.wait()

        # i*pi is a root of g
        ipi_g = Tex(r"$i\pi$ es raíz de $g$", font_size = fs, color=WHITE).next_to(g_rational, DOWN * 3)
        ipi_g_proof_1_1 = MathTex(r"g(i\pi) ")
        ipi_g_proof_1_2 = MathTex(r"= f(i^2\pi)f(-i^2\pi)", font_size = fs).next_to(ipi_g_proof_1_1, RIGHT)
        ipi_g_proof_1 = VGroup(ipi_g_proof_1_1, ipi_g_proof_1_2).next_to(ipi_g, DOWN)
        ipi_g_proof_2 = MathTex(r"= f(-(\sqrt{-1})^2\pi)f(-(\sqrt{-1})^2\pi)", font_size=fs).next_to(ipi_g_proof_1, DOWN)
        ipi_g_proof_3 = MathTex(r"= f(-\pi)f(\pi)", font_size=fs).next_to(ipi_g_proof_2, DOWN)
        ipi_g_proof_4 = MathTex(r"= 0", font_size=fs).next_to(ipi_g_proof_3, DOWN)

        self.play(Write(ipi_g))
        self.play(Write(ipi_g_proof_1), run_time=2)
        self.play(Write(ipi_g_proof_2), run_time=2)
        self.play(Write(ipi_g_proof_3), run_time=2)
        self.play(Write(ipi_g_proof_4), run_time=2)
        self.wait()

        self.play(
            FadeOut(ipi_g_proof_1_2),
            FadeOut(ipi_g_proof_2),
            FadeOut(ipi_g_proof_3),
            ipi_g_proof_1_1.animate.next_to(ipi_g, DOWN).shift([-0.4, 0, 0]),
            ipi_g_proof_4.animate.next_to(ipi_g, DOWN).shift([0.6, -0.05, 0])
        )
        self.play(ipi_g.animate.set_color(ORANGE))
        self.play(ipi_g.animate.shift([0, 0.5, 0]), FadeOut(ipi_g_proof_1_1), FadeOut(ipi_g_proof_4))
        self.wait()

        # Conclusion: i*pi is algebraic
        g_no_nulo = Tex(r"g no es el polinomio nulo", font_size = fs, color = ORANGE).next_to(ipi_g, DOWN)
        statements = VGroup(g_rational, ipi_g, g_no_nulo)
        brace = Brace(Line(LEFT * 0.9, RIGHT * 0.9)).rotate(PI/2).next_to(statements, RIGHT)
        imply = Tex(r"$\Longrightarrow$", font_size = fs).next_to(statements, DOWN + LEFT).shift([1.6, -0.4, 0])
        ipi_alg = Tex(r"$i\pi$ es algebraico", font_size = fs, color=ORANGE).next_to(imply, RIGHT)


        self.play(Write(g_no_nulo))
        self.play(Write(brace), Write(imply), Write(ipi_alg))
        self.wait()

        # By facts in legend, we find a contradiction
        self.play(FadeOut(g_rational), FadeOut(ipi_g), FadeOut(g_no_nulo), FadeOut(brace), FadeOut(imply), FadeOut(g))
        fact_1_copy = fact_1.copy()

        self.play(fact_1_copy.animate.next_to(ipi_alg, UP * 1.2))
        self.play(fact_1_copy.animate.scale(1.4))
        self.wait(2)
        e_pii = Tex(r"$e^{i\pi}$ es transcendental", font_size = fs*1.5, color = BLUE).move_to(ipi_alg.get_center())
        self.play(Transform(ipi_alg, e_pii), FadeOut(fact_1_copy))
        self.wait(2)
        fact_2_copy = fact_2.copy().next_to(ipi_alg, UP * 1.2).scale(1.6)
        fact_2_copy2 = fact_2.copy()
        self.add(fact_2_copy2)
        self.play(Transform(fact_2, fact_2_copy))
        self.wait(2)
        cont = Tex(r"Contradicción!", font_size = fs*1.5, color = RED).move_to(ipi_alg.get_center())
        self.play(Transform(ipi_alg, cont), FadeOut(fact_2))
        self.wait(2)
        cross = Cross(sup_group, scale_factor = 0.85)
        self.play(Create(cross), run_time = 2.0)
        self.wait(2)
        cont_arrow = Tex("$\Longrightarrow$").rotate(-PI/2).next_to(cont, DOWN)
        pi_trans = Tex("$\pi$ es transcendental!", color = BLUE).next_to(cont_arrow, DOWN)
        self.play(AnimationGroup(Create(cont_arrow), Write(pi_trans), lag_ratio = 0.5, run_time = 2.0))
        self.play(ShowPassingFlash(Underline(pi_trans, color = BLUE_A), time_width = 0.3), run_time = 1.0)
        self.wait(3)
