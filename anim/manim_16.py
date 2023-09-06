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
        out_rect_2 = Rectangle(width=6, height=4, color=PURPLE, grid_xstep=3.0)

        self.play(Write(out_rect_1))
        self.play(Write(real_numbers_text))
        self.wait()
        self.play(Transform(out_rect_1, out_rect_2))
        self.wait()

        # Color each part (rationals, irrationals) and add text 
        rationals_box = Rectangle(width=3, height=4, color=ORANGE, stroke_width=2)
        rationals_text = MathTex(r"\mathbb{Q}").scale(1.3).move_to(rationals_box.get_center())
        rationals = VGroup(rationals_box, rationals_text)
        irrationals_box = Rectangle(width=3, height=4, color=BLUE, stroke_width=2)
        irrationals_text = MathTex(r"\mathbb{I}").scale(1.3)
        irrationals = VGroup(irrationals_box, irrationals_text)
        reals = VGroup(rationals, irrationals)
        reals.arrange_in_grid(rows=1, cols=2, buff=0)

        self.play(AnimationGroup(
            FadeOut(out_rect_2),
            FadeIn(reals)
        ))
        self.wait(2)

    
        # Create a background color for the rationals representing that they are all algebraic
        self.play(
            rationals_box.animate.set_fill(opacity=0.5, color=RED)
        )
        self.wait(2)

        # Create a legend
        legend_algs_box = Square(color=RED, side_length=0.5, fill_color=RED, fill_opacity=0.5).shift([-2, -3, 0])
        legend_algs_text = MathTex(r"\text{Algebraicos}").scale(0.5).next_to(legend_algs_box, RIGHT)
        self.play(
            Write(legend_algs_box),
            Write(legend_algs_text)
        )
        self.wait(2)

        # Divide irrationals into algebraic and trascendentals
        alg_irrationals_box = Rectangle(width=1, height=4, color=RED, fill_color = RED, fill_opacity = 0.5).shift([0.5, 0, 0])
        tras_irrationals_box = Rectangle(width=2, height=4, color=BLUE, fill_color = BLUE, fill_opacity = 0.5).shift([2, 0, 0])
        # Complete the legend
        legend_tras_box = Square(color=BLUE, side_length=0.5, fill_color=BLUE, fill_opacity=0.5).next_to(legend_algs_text, RIGHT)
        legend_tras_text = MathTex(r"\text{Trascendentales}").scale(0.5).next_to(legend_tras_box, RIGHT)
        self.add_foreground_mobject(irrationals_text)
        self.play(
            FadeIn(alg_irrationals_box),
            FadeIn(tras_irrationals_box),
            Write(legend_tras_box),
            Write(legend_tras_text)
        )

        self.wait(2)


