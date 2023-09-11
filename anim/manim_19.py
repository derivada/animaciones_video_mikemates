from manim import *
from numpy import *
from utils import *
import matplotlib.colors as mcolors

import mpmath

fs = 40
def zeta(z):
    max_norm = 10
    try:
        return complex(mpmath.zeta(z))
    except:
        return complex(max_norm, 0)


def interpolate_color(t):
    # Define the start and end colors as RGB tuples
    start_color = mcolors.to_rgba('#ffc600')
    end_color = mcolors.to_rgba('#072ac8')
    
    # Interpolate in RGB color space
    interpolated_color = [
        start_color[i] + (end_color[i] - start_color[i]) * t
        for i in range(3)
    ]
    
    # Convert back to hex
    return mcolors.rgb2hex(interpolated_color)


class manim_19(ThreeDScene):

    def construct(self):
        # Define the background plane
        zPlane = ComplexPlane(
            x_range = [-7, 7],
            y_range = [-5, 5],
            background_line_style = {
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )

        zPlane.add_coordinates()
        self.play(Create(zPlane))
        self.wait()

        # Define the zeta function
        zeta_text = MathTex(r"\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + ...", font_size = fs)
        zeta_text.to_corner(UL)
        self.play(Write(zeta_text))

        # Define the Riemann Hypothesis
        zeta_hip = Tex(r"$\zeta(s) = 0,$ $\forall s=\frac{1}{2} + ti $", font_size = fs)
        zeta_hip.next_to(zeta_text, DOWN)
        self.play(Write(zeta_hip))

        self.wait()

        question_mark = Tex(r"?", font_size = fs, color="#ffc600").next_to(zeta_hip, RIGHT)
        self.play(Write(question_mark))
        self.wait()

        # Dot that will move along the critical line
        dot1 = Dot(point = zPlane.n2p(complex(-1.5, 0)), color = ORANGE, radius = 0.1)
        self.add(dot1)

        # Move the dot along the critical line
        for i in range(0, 1000, 1):
            t = i/10        # t = 0, 0.1, 0.2, ..., 99.9, 100
            s = complex(0.5, t)     # s = 0.5 + 0.1i, 0.5 + 0.2i, ..., 0.5 + 9.9i, 0.5 + 10i
            destination = zPlane.n2p(zeta(s))     

            new_color = interpolate_color(i/1000)       # Interpolate the color from yellow to blue
            # Create a line that connects the current position of the dot with the next position
            line = Line(dot1.get_center(), destination, color = new_color)

            dot1.set_color(new_color)

            self.play(dot1.animate.move_to(destination), Create(line), run_time=0.01)
        self.wait()

