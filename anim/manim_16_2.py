from manim import *
from numpy import *
from utils import *

fs = 48
class manim_16_2(Scene):
    def construct(self):
        desc = Tex("Polinomios ").scale(1.2)
        desc2 = Tex("no nulos ").scale(1.2)
        desc3 = Tex("de ").scale(1.2)
        desc4 = Tex("coeficientes racionales").scale(1.2)
        
        desc.to_edge(UP).shift(LEFT * 4.5 + DOWN)
        desc2.next_to(desc, RIGHT)
        desc3.next_to(desc2, RIGHT)
        desc4.next_to(desc3, RIGHT)

        self.add(desc)
        self.add(desc2)
        self.add(desc3)
        self.add(desc4)
        self.wait()

        general = MathTex("p(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0").scale(1.2)
        general.next_to(desc, DOWN).shift(RIGHT * 5 + DOWN * 0.5)

        self.play(Write(general, run_time=3))
        self.wait()

        self.play(desc4.animate.set_color(YELLOW))
        self.wait()

        rational_coefs = MathTex(r"a_i \in \mathbb{Q}\quad \forall i \in \lbrace 1,\, ...,\, n \rbrace").scale(1.2)
        rational_coefs.color = YELLOW
        rational_coefs.next_to(general, DOWN).shift(DOWN * 0.5)

        self.play(Write(rational_coefs, run_time=2))
        self.wait()

        self.play(desc2.animate.set_color(MAROON))
        self.wait()

        non_zero = MathTex("a_n \\neq 0").scale(1.2)
        non_zero.next_to(rational_coefs, DOWN).shift(DOWN * 0.5)
        non_zero.color = MAROON

        self.play(Write(non_zero))
        self.wait()

        