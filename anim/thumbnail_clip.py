from manim import *
from numpy import *
from utils import *

fs = 48

class thumbnail_clip(Scene):
    def construct(self):
        title_1 = Text("La", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, 1.8, 0])
        title_2 = Text("cuadratura", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, 0.6, 0])
        title_3 = Text("del", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, -0.6, 0])
        title_4 = Text("círculo", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, -1.8, 0])
        title_group = VGroup(title_1, title_2, title_3, title_4)
        
        # need to be done this way for simultaneity
        self.play(Write(title_group, run_time = 5),
                    AnimationGroup(*[Create(Circle(color="#0d698b", radius=r).rotate(pi*r), run_time = 5/r + 2) for r in range(3, 12)], lag_ratio = 0.2),
                    AnimationGroup(*[Create(Square(color= LIGHT_GRAY, side_length=2*r).rotate(pi*r), run_time = 5/r + 2) for r in range(3, 12)], lag_ratio = 0.2),
                    *[AnimationGroup(
                         Create(Square(color=LIGHT_GRAY, side_length=0.707).rotate(PI/4).shift([sin(ang)*3.5, cos(ang)*3.5, 0])),
                         Create(Square(color="#0d698b", side_length=0.46).shift([sin(ang)*3.5, cos(ang)*3.5, 0])),
                         Create(Square(color=LIGHT_GRAY, side_length=0.27).rotate(PI/4).shift([sin(ang)*3.5, cos(ang)*3.5, 0])),
                         lag_ratio = 0.2, run_time = 2.5)
                         for ang in [0, PI, PI/2, 3*PI/2]
                    ],
                    AnimationGroup(*[
                        AnimationGroup(
                            AnimationGroup(
                                FadeIn(Circle(color="#0d698b", radius=0.5).shift([-6.5, h, 0])),
                                FadeIn(Square(color=LIGHT_GRAY, side_length=1).shift([-6.5, h, 0])),
                                FadeIn(Circle(color="#0d698b", radius=0.2).shift([-6.5, h, 0]))),
                            AnimationGroup(
                                FadeIn(Circle(color="#0d698b", radius=0.2).shift([6.5, -h, 0])),
                                FadeIn(Circle(color="#0d698b", radius=0.5).shift([6.5, -h, 0])),
                                FadeIn(Square(color=LIGHT_GRAY, side_length=1).shift([6.5, -h, 0]))),
                        ) for h in range(-6, 6)], lag_ratio = 0.2, run_time = 5),
                    AnimationGroup(*[
                        AnimationGroup(
                            AnimationGroup(
                                FadeIn(Circle(color="#0d698b", radius=0.5).shift([-4.5,h, 0])),
                                FadeIn(Square(color=LIGHT_GRAY, side_length=1).shift([-4.5, h, 0])),
                                FadeIn(Circle(color="#0d698b", radius=0.2).shift([-4.5, h, 0]))),
                            AnimationGroup(
                                FadeIn(Circle(color="#0d698b", radius=0.2).shift([4.5, -h, 0])),
                                FadeIn(Circle(color="#0d698b", radius=0.5).shift([4.5, -h, 0])),
                                FadeIn(Square(color=LIGHT_GRAY, side_length=1).shift([4.5, -h, 0]))),
                        ) for h in range(6, -6, -1)], lag_ratio = 0.2, run_time = 5)
                )
        self.wait(3)
