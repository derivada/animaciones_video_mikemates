from manim import *
from numpy import *

fs = 36

# Sección 3.1
class manim_07(Scene):
    def trazar_arco(self, arc: Arc, run_time = 2.0, show_vect = True):
        center, radius, start_angle, angle, color = arc.arc_center, arc.radius, arc.start_angle, arc.angle, arc.color
        if(show_vect):
            vect = Arrow(start = center, end = [center[0] + cos(start_angle) * radius, center[1] + sin(start_angle) * radius, center[2]], buff = 0, color = color, 
                        max_tip_length_to_length_ratio = 0.05, tip_shape = StealthTip, stroke_opacity = 0.5, fill_opacity = 0.5, stroke_width= DEFAULT_STROKE_WIDTH*0.66) 
            self.play(Create(vect), run_time = run_time/8)
            self.play(
                Create(arc),
                Rotate(vect, angle, about_point = center),
                run_time = run_time*6/8
            )
            self.play(FadeOut(vect), run_time = run_time/8)
        else:
            self.play(Create(arc), run_time = run_time)
    
    def construct(self):        
        # puntos A y B
        pA_coords, pB_coords, pC_coords, pD_coords, pE_coords = [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [3.0, 2.0, 0.0], [3.0, 3.0, 0.0], [2.0, 0.0, 0.0] # escalar todo por 2 en coordenadas de manim
        pA, pB, pC, pD, pE = Dot(pA_coords, color = BLUE), Dot(pB_coords, color = BLUE), Dot(pC_coords, color = RED), Dot(pD_coords, color = RED), Dot(pE_coords, color = RED)
        pA_label, pB_label, pC_label, pD_label, pE_label = Tex("A", font_size = fs, color = BLUE).next_to(pA, DOWN), Tex("B", font_size = fs, color = BLUE).next_to(pB, DOWN), Tex("C", font_size = fs, color = RED).next_to(pC, RIGHT), Tex("D", font_size = fs, color = RED).next_to(pD, RIGHT), Tex("E", font_size = fs, color = RED).next_to(pE, DOWN)
        line_ab, line_cd = Line(pA_coords, pB_coords, 0, color = BLUE), Line(pC_coords, pD_coords, 0, color = RED)
        line_measure_ab = DoubleArrow(pA_coords, pB_coords, color = GRAY, max_tip_length_to_length_ratio = 0.1, max_stroke_width_to_length_ratio = 3).next_to(line_ab, DOWN*1.5)
        measure_ab = Tex("2", color = GRAY).next_to(line_measure_ab, DOWN/3)
        line_measure_cd = DoubleArrow(pC_coords, pD_coords, color = GRAY, max_tip_length_to_length_ratio = 0.2, max_stroke_width_to_length_ratio = 10).next_to(line_cd, RIGHT*1.5)
        measure_cd = Tex("1", color = GRAY).next_to(line_measure_cd, RIGHT/2)
        line_measure_ae = DoubleArrow(pA_coords, pE_coords, color = GRAY, max_tip_length_to_length_ratio = 0.07, max_stroke_width_to_length_ratio = 5, buff = 0).next_to([0.5, 0.0, 0.0], DOWN*4)
        measure_ae = Tex("3", color = GRAY).next_to(line_measure_ae, DOWN/3)
        
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), FadeIn(pC), FadeIn(pC_label), FadeIn(pD), FadeIn(pD_label), lag_ratio = 0.25, run_time = 2))
        self.play(Create(line_ab), run_time = 0.5)
        self.play(Create(line_cd), run_time = 0.5)
        self.play(FadeIn(line_measure_ab), FadeIn(measure_ab), FadeIn(line_measure_cd), FadeIn(measure_cd))
        self.wait(2)
        line_cb = DashedLine(pC_coords, pB_coords, color = GREEN_B)
        parallel_line = DashedLine(pD_coords, [0.0, 0.0, 0.0], color = GREEN_B)
        self.play(Create(line_cb))
        self.play(Create(parallel_line))
        self.wait(2)
        arc = Arc(1, -PI, -PI, arc_center = pB_coords)
        self.trazar_arco(arc)
        line_ext = Line(pB_coords, [2.0, 0.0, 0.0], buff = 0, color = RED)
        self.play(AnimationGroup(Create(line_ext), FadeIn(pE), FadeIn(pE_label), FadeOut(arc), lag_ratio = 0.2, run_time = 1))
        self.play(FadeIn(line_measure_ae), FadeIn(measure_ae))
        self.wait(3)