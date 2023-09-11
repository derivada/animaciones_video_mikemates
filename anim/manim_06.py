from manim import *
from numpy import *
from utils import trazar_arco

point_color = BLUE
arc_thick, arc_opacity, arc_color = DEFAULT_STROKE_WIDTH * 0.8, 0.6, BLUE
fs = 36

# Sección 4.4
class manim_06(Scene):
    def construct(self):        
        # puntos A y B
        pA_coords, pB_coords = [-1.0, 0.0, 0.0], [1.0, 0.0, 0.0] # escalar todo por 2 en coordenadas de manim
        pA, pB = Dot(pA_coords, color = point_color), Dot(pB_coords, color = point_color)
        pA_label, pB_label = Tex("A", font_size = fs, color = point_color).next_to(pA, DR/2), Tex("B", font_size = fs, color = point_color).next_to(pB, DR/2)
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pA_label), FadeIn(pB), FadeIn(pB_label), lag_ratio = 0.25, run_time = 2))
        self.wait(2)

        # renombrar puntos a 0 y 1
        p0_label, p1_label = Tex("0", font_size = fs, color = point_color).next_to(pA, DR/2), Tex("1", font_size = fs, color = point_color).next_to(pB, DR/2)
        self.play(AnimationGroup(Transform(pA_label, p0_label), Transform(pB_label, p1_label)))
        self.play(Indicate(pA_label))
        self.play(Indicate(pB_label))
        self.wait(2)

        # linea 0-1
        line_01 = Line(pA_coords, pB_coords, buff = DEFAULT_DOT_RADIUS)
        self.play(Create(line_01))
        self.wait(2)

        # extender linea 0-1
        line_left = Line(pA_coords, [-10.0, 0.0, 0.0], buff = DEFAULT_DOT_RADIUS)
        line_right = Line(pB_coords, [10.0, 0.0, 0.0], buff = DEFAULT_DOT_RADIUS)
        self.play(Create(line_left), Create(line_right))
        self.wait(2)

        # hallar linea numerica
        for i in range(1, 3): # i = centro (coord. x)
            arc = Arc(arc_center = [float(i)*2, 0.0, 0.0], start_angle = -PI, angle = PI, radius = 1, stroke_width = arc_thick, stroke_color = arc_color)
            trazar_arco(self, arc)
            p = Dot([i*2+1.0, 0.0, 0.0], color = point_color)
            p_label = Tex(str(i+1), font_size = fs, color = point_color).next_to(p, DR/2)
            self.play(AnimationGroup(FadeIn(p), FadeIn(p_label), lag_ratio = 0.25, run_time = 2))
            self.play(FadeOut(arc))
            self.play(Indicate(p_label, color = BLUE))
        dots = Tex("...", font_size = fs, color = point_color).move_to([6.0, -0.4, 0.0])
        self.play(FadeIn(dots))

        # extender eje vertical
        minus1_dot = Dot([-3.0, 0.0, 0.0], color = point_color)
        minus1_label = Tex("-1", font_size = fs, color = point_color).next_to(minus1_dot, DL/2)
        minus1 = VGroup(minus1_dot, minus1_label)
        minus2_dot = Dot([-5.0, 0.0, 0.0], color = point_color)
        minus2_label = Tex("-2", font_size = fs, color = point_color).next_to(minus2_dot, DL/2)
        minus2 = VGroup(minus2_dot, minus2_label)
        left_dots =  Tex("...", font_size = fs, color = point_color).move_to([-6.0, -0.4, 0.0])
        line_up = Line(pA_coords, [-1.0, 10.0, 0.0], buff = DEFAULT_DOT_RADIUS)
        line_down = Line(pA_coords, [-1.0, -10.0, 0.0], buff = DEFAULT_DOT_RADIUS)
        self.play(Create(line_up), Create(line_down), FadeIn(minus1), FadeIn(minus2), FadeIn(left_dots))
        self.wait(2)

        # cuadricula
        grid = NumberPlane(
            x_range = (-config["frame_x_radius"] - 4, config["frame_x_radius"] + 4, 2),
            y_range = (-config["frame_y_radius"], config["frame_y_radius"], 2),
            background_line_style={
                "stroke_color": GRAY_B,
                "stroke_width": DEFAULT_STROKE_WIDTH * 0.6,
                "stroke_opacity":  0.3
            },
        ).shift(LEFT)
        self.play(FadeIn(grid), FadeOut(line_up), FadeOut(line_down), FadeOut(line_01), FadeOut(line_left), FadeOut(line_right))
        self.bring_to_back(grid) # no se ve tan mal I guess
        self.wait(2)

        pUnknown = Dot([0.23398, 0.0, 0.0], color = YELLOW)
        pUnknown_label = Tex("?", font_size = fs, color = YELLOW).next_to(pUnknown, DOWN)
        self.play(AnimationGroup(FadeIn(pUnknown), FadeIn(pUnknown_label), lag_ratio = 0.5, run_time = 2))
        self.wait(1)
        arrow = Arrow(start = [2.23, 2.0, 0.0], end = pUnknown.get_center(), color = YELLOW_D)
        pregunta = Tex("¿Qué distancias podemos construir?", font_size = 24, color = YELLOW_D).next_to(arrow, UP * 2/3 + RIGHT * 1/2) # looks good to me
        self.play(AnimationGroup(FadeIn(arrow), DrawBorderThenFill(pregunta), lag_ratio = 0.5, run_time = 2))
        self.wait(3)