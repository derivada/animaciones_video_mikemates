from manim import *
from numpy import *
from utils import *

fs = 48
ORIGIN = [0, 0, 0]
COLOR_A = GOLD

class manim_21(Scene):
    def construct(self):
        ax = Axes(
            x_range = [-6, 6, 1],
            y_range = [-6, 6, 1],
            x_length = 12,
            y_length = 6,
            tips = False,
            axis_config={
                "include_numbers": False,
                "include_ticks": False,
                "stroke_color": WHITE,
                "stroke_width": 2,
            }
        )

        a_coords = ax.c2p(1, 0, 0)
        line_a = Line(ORIGIN, a_coords, color = COLOR_A)
        label_a = Tex("a", color = COLOR_A, font_size = fs).next_to(line_a, DOWN * 0.5)


        self.play(Create(ax))
        self.play(Create(line_a), Write(label_a))

        a = line_a.get_length()
        circle = Circle(radius = a, color = GOLD, fill_opacity=0.4, fill_color=GOLD_A)
        area = Tex(r"Área = $a^2\pi$", font_size = fs, color=COLOR_A).next_to(circle, DOWN * 1.5 + RIGHT * 1.5)
        self.play(DrawBorderThenFill(circle))
        self.play(Write(area))
        self.wait()
        self.play(
            circle.animate.move_to([4, 2.7, 0]),
            area.animate.move_to([4, 1.2, 0]),
        )

        # Polar coordinates: r = a * theta
        # Cartesian coordinates: x = a * theta * cos(theta), y = a * theta * sin(theta)  
        spiral = ParametricFunction(
            lambda t: np.array([
                a * t * np.cos(t),
                a * t * np.sin(t),
                0
            ]), t_range=[0, 10, 0.05], color = GOLD
        )

        spiral_text_1 = Tex(r"Espiral de Arquímedes", font_size = fs, color=COLOR_A).to_corner(UL).shift(DOWN + RIGHT)
        spiral_text_2 = Tex(r"$r = a \theta$, $a > 0$", font_size = fs, color=COLOR_A).next_to(spiral_text_1, DOWN).next_to(spiral_text_1, DOWN).align_to(spiral_text_1, LEFT)
        self.play(Create(spiral), run_time = 2)
        self.play(Write(spiral_text_1), Write(spiral_text_2))
        self.wait()

        intersection = ax.coords_to_point(0, a * PI, 0)
        dot = Dot(intersection, color = TEAL)
        label_intersection = Tex(r"$\frac{a \pi}{2}$", font_size = fs, color = TEAL).next_to(dot, DOWN * 1.5 + LEFT * 0.5)

        self.play(Create(dot), Write(label_intersection))

        rect = Rectangle(height = a * PI / 2, width = 2 * a, color = TEAL, fill_opacity=0.4, fill_color=TEAL_A).move_to([0 , a * PI / 4, 0])
        area_rect = Tex(r"Área = $2a \frac{a\pi}{2}$ = $a^2\pi$", font_size = fs, color=TEAL).next_to(rect, DOWN * 1.5 + RIGHT)

        self.play(DrawBorderThenFill(rect), FadeOut(spiral_text_1), FadeOut(spiral_text_2))
        self.play(Write(area_rect))
        self.wait()

        circle_copy = circle.copy()
        square = Square(side_length = a * sqrt(PI), color = TEAL, fill_opacity=0.4, fill_color=TEAL_A).next_to(area_rect, DOWN)
        circle_copy.move_to(square.get_center())

        self.play(Transform(rect, square))
        self.play(Transform(circle, circle_copy))

        self.wait()
        text = Text("Si tan solo la espiral", font_size = fs * 0.7, color=WHITE).to_corner(UL).shift(DOWN * 0.5 + RIGHT * 0.5)
        text_2 = Text("fuese construible con", font_size = fs * 0.7, color=WHITE).next_to(text, DOWN).align_to(text, LEFT)
        text_3 = Text("regla y compás...", font_size = fs * 0.7, color=WHITE).next_to(text_2, DOWN).align_to(text, LEFT)

        self.play(AnimationGroup(Write(text), Write(text_2), Write(text_3), lag_ratio=0.5))

        self.wait(3)