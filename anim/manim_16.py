from manim import *
from numpy import *
from utils import *

fs = 48
class manim_16(Scene):
    def construct(self):

        # Create first rectangle representing all real numbers
        out_rect_1 = Rectangle(width=6, height=4)
        real_numbers_text = MathTex(r"\mathbb{R}").scale(1.3)
        real_numbers_text.align_to(out_rect_1, UP + LEFT).shift([-0.7, 0, 0])

        # Divide the rectangle into two parts
        out_rect_2 = Rectangle(width=6, height=4, grid_xstep=3.0)

        self.play(Write(out_rect_1))
        self.play(Write(real_numbers_text))
        self.wait()
        self.play(Transform(out_rect_1, out_rect_2))
        self.wait()

        # Color each part (rationals, irrationals) and add text 
        rationals_box = Rectangle(width=3, height=4, stroke_width=2)
        rationals_text = MathTex(r"\mathbb{Q}").scale(1.3).move_to(rationals_box.get_center())
        rationals = VGroup(rationals_box, rationals_text)
        irrationals_box = Rectangle(width=3, height=4, stroke_width=2)
        irrationals_text = MathTex(r"\mathbb{I}").scale(1.3)
        irrationals = VGroup(irrationals_box, irrationals_text)
        reals = VGroup(rationals, irrationals)
        reals.arrange_in_grid(rows=1, cols=2, buff=0)

        self.play(AnimationGroup(
            FadeOut(out_rect_1),
            FadeOut(out_rect_2),
            FadeIn(reals)
        ))
        self.wait(2)

        # Create a legend
        legend_algs_box = Square(color=RED, side_length=0.5, fill_color=RED, fill_opacity=0.5).shift([-2, -3, 0])
        legend_algs_text = MathTex(r"\text{Algebraicos}").scale(0.5).next_to(legend_algs_box, RIGHT)
        legend_tras_box = Square(color=BLUE, side_length=0.5, fill_color=BLUE, fill_opacity=0.5).next_to(legend_algs_text, RIGHT)
        legend_tras_text = MathTex(r"\text{Trascendentales}").scale(0.5).next_to(legend_tras_box, RIGHT)
        self.play(
            Write(legend_algs_box),
            Write(legend_algs_text),
            Write(legend_tras_box),
            Write(legend_tras_text)
        )
        self.wait(2)

        # Move everything to the left
        self.play(
            real_numbers_text.animate.shift(LEFT * 2.5),
            reals.animate.shift(LEFT * 2.5),
            legend_algs_box.animate.shift(LEFT * 2.5),
            legend_algs_text.animate.shift(LEFT * 2.5),
            legend_tras_box.animate.shift(LEFT * 2.5),
            legend_tras_text.animate.shift(LEFT * 2.5)
        )
        self.wait(2)

        dot_2 = Dot(color=WHITE).scale(0.5).align_to(rationals_box, LEFT + UP).shift([0.5, -0.5, 0])
        dot_2_text = MathTex(r"2").next_to(dot_2, RIGHT)
        eq_2 = MathTex(r"x - 2 = 0").scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])

        self.play(
            Write(dot_2),
            Write(dot_2_text)
        )
        self.play(Write(eq_2))
        self.play(
            dot_2.animate.set_color(RED),
            dot_2_text.animate.set_color(RED)
        )
        self.wait(2)

        dot_p_q = Dot(color=WHITE).scale(0.5).align_to(rationals_box, LEFT + DOWN).shift([1, 0.5, 0])
        dot_p_q_text = MathTex(r"\frac{p}{q} \in \mathbb{Q}").scale(0.8).next_to(dot_p_q, RIGHT)
        eq_p_q = MathTex(r"qx - p = 0").scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])

        self.play(FadeOut(dot_2), FadeOut(dot_2_text), Write(dot_p_q), Write(dot_p_q_text))   
        self.play(Transform(eq_2, eq_p_q))
        self.wait()

        # Create a background color for the rationals representing that they are all algebraic
        self.play(FadeOut(dot_p_q), FadeOut(dot_p_q_text), FadeOut(eq_p_q), FadeOut(eq_2),
            rationals_box.animate.set_fill(opacity=0.5, color=RED)
        )
        self.wait(2)


        dot_sqrt_2 = Dot(color=WHITE).scale(0.5).align_to(irrationals_box, UP).shift([0, -0.5, 0])
        dot_sqrt_2_text = MathTex(r"\sqrt{2}").next_to(dot_sqrt_2, LEFT)
        eq_sqrt_2 = MathTex(r"x^2 - 2 = 0").scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])
        self.play(Write(dot_sqrt_2), Write(dot_sqrt_2_text), Write(eq_sqrt_2))
        self.wait()


        # Divide irrationals into algebraic and trascendentals
        alg_irrationals_box = Rectangle(width=3, height=1, fill_color = RED, fill_opacity = 0.5).align_to(irrationals_box, RIGHT + UP)

        self.add_foreground_mobject(irrationals_text)
        self.play(
            FadeIn(alg_irrationals_box)
        )
        self.wait(2)

        tras_irrationals_box = Rectangle(width=3, height=3, fill_color = BLUE, fill_opacity = 0.5).align_to(irrationals_box, RIGHT + DOWN)
        self.play(
            FadeOut(dot_sqrt_2),
            FadeOut(dot_sqrt_2_text),
            FadeOut(eq_sqrt_2),
            FadeIn(tras_irrationals_box)
        )
        self.wait(2)
        quest = Tex("?", font_size = fs*1.25).move_to(tras_irrationals_box.get_center()).shift(DOWN/2)
        self.play(Write(quest), run_time = 1.5)
        self.wait(3)
        n_e = Tex("$e^a$", font_size = fs).next_to(irrationals_text, LEFT*2.75 + UP)
        n_e_alg = Tex("(a algebraico)", font_size = fs*0.66).next_to(n_e, RIGHT).align_to(n_e, DOWN)
        n_pi_quest = Tex("¿$\pi$?", font_size = fs*1.25).next_to(irrationals_text, DOWN*1.5+RIGHT*0.2)
        n_e_line = VGroup(n_e, n_e_alg)
        n_liou = Tex("$L_b$", font_size = fs).next_to(n_pi_quest, LEFT*2 + DOWN * 0.6)
        self.play(AnimationGroup(FadeOut(quest), Write(n_e_line), Write(n_liou), Write(n_pi_quest), lag_ratio = 0.5, run_time = 2.5))
        self.wait(1)
        self.play(Indicate(n_pi_quest, color = BLUE_D), run_time = 2)
        self.wait(3)
        

