from manim import *
from numpy import *
from utils import *

fs = 40
aux_thick, aux_arc_len = DEFAULT_STROKE_WIDTH * 0.6, PI/16

# Sección 4.1
class manim_17(MovingCameraScene):
    def construct(self):
        # We will leave a gap above for the images of the compass & straightedge
        # They should be added in DaVinci, and the video should start showing them before any animation

        self.wait(3)

        # Line construction on the left of the screen
                
        # Axes of reference
        axes = Axes(
            x_range=(-3.5, 3, 1),
            y_range=(-2.5, 4, 1),
            x_length=5,
            y_length=3.5,
            axis_config={'tip_shape': StealthTip}
        ).move_to(LEFT*4 + DOWN * 1.5)

        labels = axes.get_axis_labels(
            Tex("x").scale(0.8), Text("y").scale(0.5)
        )

        # Red line
        line = axes.plot_line_graph(
            x_values = [-3, 2],
            y_values = [-2, 3],
            line_color=RED,
            stroke_width = 4,
            add_vertex_dots=False,
        )
        

        line_eq = MathTex(r"y = ax + b", font_size = fs, color = RED)
        line_eq.next_to(line, UR, 0.2)

        # Points to be used in identifying the slope
        d1 = Dot(axes.coords_to_point(*[0, 1, 0]), color=PURPLE)  
        d2 = Dot(axes.coords_to_point(*[1, 2, 0]), color=PURPLE)

        b_label = MathTex(r"b", font_size = fs, color = TEAL).next_to(d1, LEFT * 0.5 +  UP * 0.5)

        ref_point = Dot(axes.coords_to_point(1, 1, 0), stroke_width=0, fill_opacity=0)
        # We shift the reference point so that the absence of a dot is not noticeable
        h_line = Line(d1.get_center(), ref_point.shift([0.1, 0, 0]), color=PURPLE)
        h_line_label = MathTex(r"\Delta x", font_size = fs * 0.8, color = PURPLE).next_to(h_line, DOWN * 0.5)
        # We reverse the shift to the right on the reference point and then apply a slight shift downwards
        v_line = Line(d2.get_center(), ref_point.shift([-0.1, -0.1, 0]), color=PURPLE)
        v_line_label = MathTex(r"\Delta y", font_size = fs * 0.8, color = PURPLE).next_to(v_line, RIGHT * 0.5)

        a = MathTex(r"a = \frac{\Delta y}{\Delta x}", font_size = fs, color = TEAL).next_to(line_eq, DOWN)

        # First, show the line
        self.play(Create(line))
        self.wait(2)
        # Then add the axes below
        self.play(Create(axes), Write(labels))
        self.play(Write(line_eq))
        # Show the meaning of a and b
        self.play(Create(d1), Create(d2))
        self.play(Create(h_line), Create(v_line), Write(h_line_label), Write(v_line_label))
        self.play(Write(a), Write(b_label), d1.animate.set_color(TEAL))
        self.wait()


        # Right side of the screen - circunference construction

        # Axes of reference
        axes = Axes(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=4,
            y_length=4,
            axis_config={'tip_shape': StealthTip}
        ).move_to(RIGHT*4 + DOWN * 1.5)

        labels = axes.get_axis_labels(
            Tex("x").scale(0.8), Text("y").scale(0.5)
        )


        # Blue center
        c = Dot(axes.c2p(0, 0, 0), color=PURPLE, stroke_width=4)
        c_label = MathTex(r"c", font_size = fs, color = PURPLE).next_to(c, DOWN * 0.5).shift([0.3, 0, 0])
        # Radius = 2 in the axes reference
        circle_arc = Arc(arc_center = c.get_center(), start_angle = PI/2, angle = 2*PI, radius = 1, stroke_color = BLUE)
        radius_line = Line(c.get_center(), circle_arc.get_start(), color=PURPLE, stroke_width=7)
        radius_label = MathTex(r"r", font_size = fs, color = PURPLE).next_to(radius_line, LEFT)
        c_label_2 = MathTex(r"c = (c_x, c_y)", font_size = fs, color = PURPLE).next_to(circle_arc, UR).shift([-0.5, -0.2, 0])
        circle_eq = MathTex(r"(x-c_x)^2 + (y-c_y)^2 = r^2", font_size = fs * 1.1, color = BLUE).next_to(circle_arc, DL).shift([1, 0, 0])

        self.play(Create(c))
        trazar_arco(self, circle_arc)
        self.wait(2)
        self.play(Create(axes), Write(labels))
        self.play(Write(c_label), Create(radius_line), Write(radius_label), Write(c_label_2))
        self.play(Write(circle_eq))
        self.wait()

        