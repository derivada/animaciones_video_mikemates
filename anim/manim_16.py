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
        rationals_box = Rectangle(width=3, height=4)
        rationals_text = MathTex(r"\mathbb{Q}").scale(1.3).move_to(rationals_box.get_center())
        rationals = VGroup(rationals_box, rationals_text)
        irrationals_box = Rectangle(width=3, height=4)
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

        text_2 = MathTex(r"2", font_size = 1.25*fs).align_to(rationals_box, LEFT + UP).shift([0.5, -0.5, 0])
        eq_2 = MathTex(r"x - 2 = 0").scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])

        self.play(
            Write(text_2)
        )
        self.play(Write(eq_2))
        self.play(
            text_2.animate.set_color(WHITE)
        )
        self.wait(2)

        text_pq = MathTex(r"\frac{p}{q}", font_size = fs*1.25).align_to(rationals_box, LEFT + DOWN).shift([2.25, 0.5, 0])
        eq_p_q = MathTex(r"qx - p = 0", font_size = fs).scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])

        self.play(FadeOut(text_2), Write(text_pq))   
        self.play(Transform(eq_2, eq_p_q))
        self.wait()

        # Create a background color for the rationals representing that they are all algebraic
        self.play(FadeOut(text_pq), FadeOut(eq_p_q), FadeOut(eq_2),
            rationals_box.animate.set_fill(opacity=0.5, color=RED)
        )
        self.wait(2)

        text_sqrt2 = MathTex(r"\sqrt{2}", font_size = fs).move_to([-1.75, 1.5, 0.0])
        eq_sqrt_2 = MathTex(r"x^2 - 2 = 0").scale(2).next_to(irrationals, RIGHT).shift([1, 0, 0])
        self.play(Write(text_sqrt2), Write(eq_sqrt_2))
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
            FadeOut(text_sqrt2),
            FadeOut(eq_sqrt_2),
            FadeIn(tras_irrationals_box)
        )
        self.wait(2)
        quest = Tex("?", font_size = fs*1.25).move_to(tras_irrationals_box.get_center()).shift(DOWN/2)
        self.play(Write(quest), run_time = 1.5)
        self.wait(3)
        text_e = Tex("$e^a$", font_size = fs).next_to(irrationals_text, LEFT*2.75 + UP)
        text_e_sub = Tex("(a algebraico)", font_size = fs*0.66).next_to(text_e, RIGHT).align_to(text_e, DOWN)
        text_pi_quest = Tex("¿$\pi$?", font_size = fs*1.25).next_to(irrationals_text, DOWN*1.5+RIGHT*0.2)
        text_e_line = VGroup(text_e, text_e_sub)
        text_liou = Tex("$L_b$", font_size = fs).next_to(text_pi_quest, LEFT*2 + DOWN * 0.6)
        self.play(AnimationGroup(FadeOut(quest), Write(text_e_line), Write(text_liou), Write(text_pi_quest), lag_ratio = 0.5, run_time = 2.5))
        self.wait(1)
        self.play(Indicate(text_pi_quest, color = BLUE_D), run_time = 2)
        self.wait(3)
        
        # corte a  5.7
        text_pi = Tex("$\pi$", font_size = fs).next_to(irrationals_text, DOWN*1.5+RIGHT*0.2)
        self.remove(text_pi_quest)
        self.add(text_2, text_pq, text_sqrt2, text_pi)
        self.wait(1)
        legend_constr_box = Square(color=GREEN, side_length=0.5, fill_color=GREEN, fill_opacity=0.5).next_to(legend_tras_text, RIGHT)
        legend_constr_text = MathTex(r"\text{Construibles}").scale(0.5).next_to(legend_constr_box, RIGHT)

        constr_box = Polygon([-5.5, 2.0, 0.0], [-5.5, -2.0, 0.0], [-2.5, -2.0, 0.0], [-2.5, 1.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, 2.0, 0.0], 
                            color = GREEN, fill_opacity = 0.5)
        self.play(
            AnimationGroup(Write(legend_constr_box), Write(legend_constr_text), FadeIn(constr_box), lag_ratio = 0.5, run_time = 3.0)
        )
        self.wait(3)

        coords = [4.5, 3.0, 0.0]
        pi_trans = Tex(r"$\pi$", font_size = fs, color = BLUE)
        pi_trans_text = Tex(r"es transcendental", font_size = fs).next_to(pi_trans, RIGHT).align_to(pi_trans, DOWN)
        pi_trans_line = VGroup(pi_trans, pi_trans_text).move_to(coords)
        arrow_1 = Tex(r"$\Longrightarrow$", font_size = fs).rotate(-PI/2).next_to(pi_trans_line, DOWN)
        pi_not_constr = Tex(r"$\pi$", color = BLUE, font_size = fs)
        pi_not_constr_text = Tex(r"no es construible", font_size = fs).next_to(pi_not_constr, RIGHT).align_to(pi_not_constr, DOWN)
        pi_not_constr_line = VGroup(pi_not_constr, pi_not_constr_text).next_to(arrow_1, DOWN)

        self.play(Indicate(text_pi, color = BLUE_D), Write(pi_trans_line), run_time = 2)
        self.wait(2)
        self.play(FadeIn(arrow_1), Write(pi_not_constr_line), run_time = 2)

        sqrt_pi_not_constr = Tex(r"$\sqrt{\pi}$", color = BLUE, font_size = fs).move_to(pi_not_constr.get_center()).shift([-0.1, 0.0, 0.0])
        self.wait(2)
        self.play(Transform(pi_not_constr, sqrt_pi_not_constr))
        self.wait(2)

        quad_sqrtpi = Square(sqrt(pi), color = LIGHT_GRAY, fill_opacity = 0.5).next_to(pi_not_constr_line, DOWN*3).shift([0.25, 0.0, 0.0])
        sqrtpi_quad_up = Tex(r"$\sqrt{\pi}$", font_size = fs, color = LIGHT_GRAY).next_to(quad_sqrtpi, UP*0.5)
        sqrtpi_quad_left = Tex(r"$\sqrt{\pi}$", font_size = fs, color = LIGHT_GRAY).next_to(quad_sqrtpi, LEFT*0.5)
        cross = Cross(quad_sqrtpi, scale_factor = 1.1, color = RED)

        self.play(AnimationGroup(DrawBorderThenFill(quad_sqrtpi), FadeIn(sqrtpi_quad_up), FadeIn(sqrtpi_quad_left), lag_ratio = 0.25, run_time = 2.0))
        self.wait(2)
        self.play(Create(cross))
        self.wait(2)

