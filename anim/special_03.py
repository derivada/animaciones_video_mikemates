from manim import *
from numpy import *
from utils import *

fs = 48

# Sección 1.3
class special_03(Scene):
    def construct(self):    
        anax_desc = Tex("Primer matemático en trabajar en el problema", font_size = fs).shift([2.0, 2.5, 0.0])
        hipo_desc = Tex("\"Luna de Hipócrates\"", font_size = fs).shift([2.0, -1.5, 0.0]).align_to(anax_desc, LEFT)
        quad = Square(side_length = sqrt(pi), color = RED, fill_opacity = 0.5)
        equal = Tex("=", font_size = fs*2, color = WHITE).next_to(quad, RIGHT*1.5)
        circ = Circle(radius = 1, color = BLUE, fill_opacity = 0.5).next_to(equal, RIGHT*1.5)
        VGroup(quad, circ, equal).scale(0.75).shift([-2.125, 0.0, 0.0]).shift(UP)

        moon_base = Line([-1.0, 0.0, 0.0], [1.0, 0.0, 0.0])
        moon_perp = Line([0.0, 0.0, 0.0], [0.0, 1.0, 0.0])
        moon_semi = Arc(1, 0, PI, arc_center = [0.0, 0.0, 0.0])
        moon_triang = Line([-1.0, 0.0, 0.0], [0.0, 1.0, 0.0])
        moon_arc = Arc(sqrt(2)/2, PI/4, PI, arc_center = [-1/2, 1/2, 0.0])
        poly = ArcPolygonFromArcs(Arc(1, PI/2, PI/2, arc_center = [0.0, 0.0, 0.0]), moon_arc)
        mask = Circle()
        poly_real = Difference(poly, mask, fill_color = RED, fill_opacity = 0.5, stroke_width = 0)
        triang = Polygon([0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], fill_color = BLUE, fill_opacity = 0.5, stroke_width = 0)
        moon_group = VGroup(moon_base, moon_perp, moon_semi, moon_triang, moon_arc, poly_real, triang).next_to(hipo_desc, DOWN*2).scale(1.5)

        self.wait(2)
        self.play(AnimationGroup(Write(anax_desc), DrawBorderThenFill(quad), DrawBorderThenFill(circ), FadeIn(equal), lag_ratio = 0.5, run_time = 3))
        self.wait(2)
        self.play(AnimationGroup(Write(hipo_desc, run_time = 2), Create(moon_base), Create(moon_perp), Create(moon_semi), Create(moon_triang), Create(moon_arc), FadeIn(poly_real), FadeIn(triang), lag_ratio = 0.5, run_time = 3))
        self.wait(3)