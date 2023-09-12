from manim import *
from numpy import *
from utils import *

fs = 36

# Sección 2.1-2.2
class special_06(Scene):
    def construct(self):    
        p_a = Dot(color = BLUE).shift(LEFT*2)
        p_b = Dot(color = ORANGE).shift(RIGHT*2)
        label_a = Tex("A", font_size = fs, color = LIGHT_GRAY).next_to(p_a, UP)
        label_b = Tex("B", font_size = fs, color = LIGHT_GRAY).next_to(p_b, UP)
        line_ab = Line(p_a.get_center(), p_b.get_center(), buff = DEFAULT_DOT_RADIUS)
        line_group = VGroup(p_a, p_b, label_a, label_b, line_ab)

        self.play(AnimationGroup(FadeIn(p_a), FadeIn(label_a), FadeIn(p_b), FadeIn(label_b), run_time = 2, lag_ratio = 0.5))
        self.wait(2)
        self.play(Create(line_ab))
        self.wait(2)
        self.play(line_group.animate.shift(LEFT*3))

        p_o = Dot(color = BLUE).shift(RIGHT*3)
        p_c = Dot(color = ORANGE).shift(RIGHT*5)
        label_o = Tex("O", font_size = fs, color = LIGHT_GRAY).next_to(p_o, DOWN)
        label_c = Tex("C", font_size = fs, color = LIGHT_GRAY).next_to(p_c, DR)
        circle_oc = Arc(radius = 2, start_angle = 0.04, angle = 2*PI-0.08, arc_center = p_o.get_center())

        self.play(AnimationGroup(FadeIn(p_o), FadeIn(label_o), FadeIn(p_c), FadeIn(label_c), run_time = 2, lag_ratio = 0.5))
        self.wait(2)
        self.play(Create(circle_oc))
        self.wait(2)


