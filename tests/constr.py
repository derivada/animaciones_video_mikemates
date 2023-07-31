from manim import *
from numpy import cos, sin
class Triangle(Scene):
    def construct(self):
        base = Line(LEFT, LEFT, stroke_color = GREEN)
        self.play(base.animate.put_start_and_end_on(LEFT, RIGHT))
        left_arc = Arc(2, PI/4, PI/8, 9, LEFT, stroke_color = GREEN_A)
        self.play(Create(left_arc))
        right_arc = Arc(2, 3*PI/4, -PI/8, 9, RIGHT, stroke_color = GREEN_A)
        self.play(Create(right_arc))
        self.wait(1)
        inter_coords = [-1.0 + 2*cos(PI/3), 2*sin(PI/3), 0.0]
        inter = Dot(inter_coords, color = BLUE, stroke_width=1)
        self.play(FadeIn(inter, run_time = 1), FadeOut(left_arc, run_time = 2), FadeOut(right_arc, run_time = 2))
        line1 = Line(LEFT, inter_coords, stroke_color = GREEN)
        line2 = Line(RIGHT, inter_coords, stroke_color = GREEN)
        self.play(Create(line1), Create(line2), FadeOut(inter))
        triangle = Polygon(LEFT, RIGHT, inter_coords, stroke_color = GREEN)
        self.play(FadeIn(triangle, run_time = 0.2))
        self.wait(2)
        
