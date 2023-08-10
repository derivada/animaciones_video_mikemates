from manim import *
from numpy import *

point_thick = DEFAULT_STROKE_WIDTH * 0.3
line_thick, line_color = DEFAULT_STROKE_WIDTH, WHITE
grid_thick, grid_color, grid_opacity = DEFAULT_STROKE_WIDTH * 0.6, GRAY_B, 0.4
arc_thick, arc_color = DEFAULT_STROKE_WIDTH * 0.8, BLUE
aux_thick = DEFAULT_STROKE_WIDTH * 0.6

fs = 36

# Sección 3.1
class manim_06(Scene):
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
        pA_coords, pB_coords = [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0] # escalar todo por 2 en coordenadas de manim
        pA, pB = Dot(pA_coords, stroke_width = point_thick), Dot(pB_coords, stroke_width = point_thick)
        pA_label, pB_label = Tex("A", font_size = fs).next_to(pA, DR/2), Tex("B", font_size = fs).next_to(pB, DR/2)
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), lag_ratio = 0.25, run_time = 2))
        self.wait(2)

        # renombrar puntos a 0 y 1
        p0_label, p1_label = Tex("0", font_size = fs).next_to(pA, DR/2), Tex("1", font_size = fs).next_to(pB, DR/2)
        self.play(AnimationGroup(Transform(pA_label, p0_label), Transform(pB_label, p1_label)))
        self.play(Indicate(pA_label, color = BLUE))
        self.play(Indicate(pB_label, color = BLUE))
        self.wait(2)

        # linea 0-1
        line_01 = Line(pA_coords, pB_coords, buff = 0, stroke_width = line_thick, color = line_color)
        self.play(Create(line_01))
        self.wait(2)

        # extender linea 0-1
        line_left = Line(pA_coords, [-10.0, 0.0, 0.0], buff = 0, stroke_width = line_thick, color = line_color)
        line_right = Line(pB_coords, [10.0, 0.0, 0.0], buff = 0, stroke_width = line_thick, color = line_color)
        self.play(Create(line_left), Create(line_right))
        self.wait(2)

        # hallar linea numerica
        for i in range(1, 3): # i = centro (coord. x)
            arc = Arc(arc_center = [float(i)*2, 0.0, 0.0], start_angle = -PI, angle = PI, radius = 1, stroke_width = arc_thick, stroke_color = arc_color)
            self.trazar_arco(arc)
            p = Dot([i*2+1.0, 0.0, 0.0], stroke_width = point_thick)
            p_label = Tex(str(i+1), font_size = fs).next_to(p, DR/2)
            self.play(AnimationGroup(FadeIn(p), FadeIn(p_label), lag_ratio = 0.25, run_time = 2))
            self.play(FadeOut(arc))
            self.play(Indicate(p_label, color = BLUE))
        dots = Tex("...", font_size = fs).move_to([6.0, -0.4, 0.0])
        self.play(FadeIn(dots))

        # extender eje vertical
        line_up = Line(pA_coords, [-1.0, 10.0, 0.0], buff = 0, stroke_width = line_thick, color = line_color)
        line_down = Line(pA_coords, [-1.0, -10.0, 0.0], buff = 0, stroke_width = line_thick, color = line_color)
        self.play(Create(line_up), Create(line_down))
        self.wait(2)

        # cuadricula
        grid = NumberPlane(
            x_range = (-config["frame_x_radius"]-4, config["frame_x_radius"]+4, 2),
            y_range = (-config["frame_y_radius"], config["frame_y_radius"], 2),
            background_line_style={
                "stroke_color": grid_color,
                "stroke_width": grid_thick,
                "stroke_opacity": grid_opacity
            }
        ).shift(LEFT)
        self.play(FadeIn(grid), FadeOut(line_up), FadeOut(line_down), FadeOut(line_01), FadeOut(line_left), FadeOut(line_right))
        self.wait(2)

        pUnknown = Dot([0.23398, 0.0, 0.0], stroke_width = point_thick, color = YELLOW)
        pUnknown_label = Tex("?", font_size = fs, color = YELLOW).next_to(pUnknown, DOWN)
        self.play(AnimationGroup(FadeIn(pUnknown), FadeIn(pUnknown_label), lag_ratio = 0.5, run_time = 2))
        self.wait(1)
        arrow = Arrow(start = [2.23, 2.0, 0.0], end = pUnknown.get_center(), color = YELLOW_D)
        pregunta = Tex("¿Qué distancias podemos construir?", font_size = 24, color = YELLOW_D).next_to(arrow, UP * 2/3 + RIGHT * 1/2) # looks good to me
        self.play(AnimationGroup(FadeIn(arrow), DrawBorderThenFill(pregunta), lag_ratio = 0.5, run_time = 2))
        self.wait(3)