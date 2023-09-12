from manim import *
from numpy import *
from utils import *

fs = 48
# add radial blur in a corner for the cool effect
class thumbnail_clip_end_bg(Scene):
    def construct(self):
        self.play(
            AnimationGroup(*[Create(Circle(color="#0d698b", radius=r).rotate(pi*r), run_time = 10/r + 2) for r in range(3, 12)], lag_ratio = 0.2),
            AnimationGroup(*[Create(Square(color= LIGHT_GRAY, side_length=2*r).rotate(pi*r), run_time = 10/r + 2) for r in range(3, 12)], lag_ratio = 0.2)
        )