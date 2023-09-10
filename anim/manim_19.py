from manim import *
from numpy import *
from utils import *

fs = 48
class manim_19(ThreeDScene):
    def construct(self):
        # Create a torus
        torus = Torus(
            major_radius=2.0,
            minor_radius=1.0,
            u_range=[0, TAU],
            v_range=[0, TAU],
            checkerboard_colors=[MAROON_A, PURPLE_A],
        )

        self.set_camera_orientation(phi=60 * DEGREES, theta=0)


        self.add(torus)

        # Move the camera along the top of the torus
        self.begin_ambient_camera_rotation(rate=0.1)


        self.wait(2)