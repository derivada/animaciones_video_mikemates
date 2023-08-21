from manim import *
from numpy import *
from utils import *

fs = 24
liou_color = BLUE
euler_color = GREEN

# Sección 5.4
class manim_13(Scene):
    def construct(self):    
        # this one was hard    
        title = Title("Primeros números transcendentales")
        self.add(title)
        timeline = NumberLine(x_range=[1840, 1880, 10], length = 10, decimal_number_config={"num_decimal_places": 0}, font_size = fs)
        dotsL = Tex("\dots", font_size = fs)
        dotsR = Tex("\dots", font_size = fs)

        # hay que añadir manualmente porque si no se muestran como 1,840 en vez de 1840
        timeline.add_labels({1840: Tex("1840"), 1850: Tex("1850"),1860: Tex("1860"),1870: Tex("1870"), 1880: Tex("1880")}, direction = DOWN, buff = 0.2, font_size = fs)
        timeline.add_ticks()
        
        timeline_group = VGroup(dotsL, timeline, dotsR).arrange()
        dotsL.shift(UP/6 + RIGHT/6)
        dotsR.shift(UP/6 + LEFT/6)
        year = Tex("Año", font_size = fs).next_to(dotsL, UP + RIGHT*0.4)
        timeline_group.add(year).shift(DOWN*2)
        self.play(FadeIn(timeline_group))
        self.wait(3)
        
        # timeline len = 10, rango = 40, cada número cada 10/40 = 0.5. el centro es 1860
        # manual positioning moment
        arrow_date = Vector(DOWN).shift([(1851-1860) * 0.25, -0.5, 0.0])
        label_1851 = DecimalNumber(1851, num_decimal_places = 0, include_sign = False, group_with_commas = False, font_size = fs*0.66, color = liou_color).move_to(timeline).shift([(1851-1860) * 0.25, 0.365, 0.0])
        tick_1851 = Rectangle(height = 0.15, width = 0.02, stroke_width = 0, fill_opacity = 1, color = liou_color).move_to(timeline).shift([(1851-1860) * 0.25, 0.13, 0.0])
        self.play(AnimationGroup(FadeIn(arrow_date), FadeIn(label_1851), FadeIn(tick_1851), lag_ratio = 0.2, run_time = 2))
        self.wait(3)

        liouville_n = Text("Número de Liouville", font_size = fs, t2c={'Liouville': liou_color}, font='Arial').next_to(arrow_date, UP)
        self.play(DrawBorderThenFill(liouville_n), run_time = 2)
        liouville = Tex(r"$$L_b = \sum^{\infty}_{n=1} \frac{1}{10^{n!}}$$").next_to(liouville_n, UP)
        liouville_expansion = Tex(r" = 0.1100010000000000000000010\dots", font_size = fs).next_to(liouville, RIGHT)
        self.play(FadeIn(liouville))
        self.wait(1)
        self.play(FadeIn(liouville_expansion))
        self.wait(3)
        self.play(FadeOut(liouville_expansion), run_time = 2)
        self.wait(1)

        label_1873 = DecimalNumber(1873, num_decimal_places = 0, include_sign = False, group_with_commas = False, font_size = fs*0.66, color = euler_color).move_to(timeline).shift([(1873-1860) * 0.25, 0.365, 0.0])
        tick_1873 = Rectangle(height = 0.15, width = 0.02, stroke_width = 0, fill_opacity = 1, color = euler_color).move_to(timeline).shift([(1873-1860) * 0.25, 0.13, 0.0])
        self.play(AnimationGroup(arrow_date.animate.shift([(1873-1851)*0.25, 0.0, 0.0]), FadeIn(label_1873), FadeIn(tick_1873), lag_ratio = 0.2, run_time = 3))

        euler_n = Text("Número de Euler", font_size = fs, t2c={'Euler': euler_color}, font='Arial').next_to(arrow_date, UP)
        self.play(DrawBorderThenFill(euler_n), run_time = 2)
        euler = Tex(r"$$e= \sum^{\infty}_{n=0} \frac{1}{n!}$$").next_to(euler_n, UP)
        euler_expansion = Tex(r" = 2.718281828\dots", font_size = fs).next_to(euler, RIGHT)
        self.play(FadeIn(euler))
        self.wait(1)
        self.play(FadeIn(euler_expansion))
        self.wait(3)
        self.play(FadeOut(euler_expansion), run_time = 2)
        self.wait(1)
        euler_general = Tex(r"$$e^a= \sum^{\infty}_{n=0} \frac{a^n}{n!}$$").next_to(euler_n, UP)
        euler_general_aclaracion = Tex("($a$ algebraico)", font_size = fs*0.66).next_to(euler_general)
        self.play(Transform(euler, euler_general))
        self.play(FadeIn(euler_general_aclaracion))
        self.wait(3)