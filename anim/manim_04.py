from manim import *
from numpy import *

circle_color, circle_thick = GREEN, DEFAULT_STROKE_WIDTH * 1.5
sq_color, sq_thick, sq_fill = BLUE, DEFAULT_STROKE_WIDTH * 1.2, BLUE_B
fs = 40

# Sección 3.7
class manim_04(MovingCameraScene):
    def construct(self):
        fs = 40 # font size
        circle = Circle(radius = 1.0, color = circle_color, stroke_width = circle_thick)
        sq = Square(side_length = 1.7, color = sq_color, fill_color = sq_fill, fill_opacity = 0.3, stroke_width = sq_thick).shift([0.2, 0.2, 0.0])
        self.add(circle)
        self.camera.frame.save_state()
        self.camera.frame.set(width = 0.8)
        # se pueden añadir más cosas más adelante
        alg_text_1 = Tex(r"$x^2 + y^2 = r^2$", font_size = fs*1.5).shift([-2.5, -2.0, 0.0])
        alg_text_2 = Tex(r"$y = mx + b$", font_size = fs*1.5).shift([2.5, 1.5, 0.0])
        alg_text_3 = Tex(r"$\begin{cases} ax + by = 0\\ cx + dy = 2\\ \end{cases}$", font_size = fs * 0.8).shift([3.0, -2.5, 0.0])
        alg_text_4 = Tex(r"$\sqrt{2\sqrt{2\sqrt{2\dots }}}$", font_size = fs*0.6).shift([-3.5, 3.0, 0.0])
        alg_text_5 = Tex(r"$\pi$", font_size = fs * 2.5).shift([0.5, 2.7, 0.0])
        alg_text_6 = Tex(r"$K | \mathbb{Q}$", font_size = fs*0.8, tex_template = TexTemplate().add_to_preamble(r"\usepackage{amssymb}")).shift([-3.0, -0.5, 0.0])
        dummy = Tex("a", font_size = 1).shift([100.0, 0.0, 0.0])

        # no sé si esta es la mejor forma de organizar las animaciones pero funciona
        anim = AnimationGroup(FadeIn(dummy, run_time = 4),
                              DrawBorderThenFill(sq, run_time = 1.0),
                              FadeIn(alg_text_1, run_time = 1.5), # delay inicial 
                              FadeIn(alg_text_2, run_time = 1.5), 
                              FadeIn(alg_text_3, run_time = 1.2),
                              FadeIn(alg_text_4, run_time = 1.7),
                              lag_ratio = 1)
        anim_2 = AnimationGroup(FadeIn(dummy, run_time = 4.5),
                                DrawBorderThenFill(alg_text_5, run_time = 1.5),
                                FadeIn(alg_text_6, run_time = 1.2), 
                                lag_ratio = 1.5)
        self.play(Restore(self.camera.frame, run_time = 10), anim, anim_2)
        self.wait(2)
        self.play(self.camera.frame.animate.set(width = 0.8), FadeOut(circle), FadeOut(sq), run_time = 1)