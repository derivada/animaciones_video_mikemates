from manim import *
from numpy import *
from utils import *

# Sección 2 intro (realmente parte 1 porque lo otro es intro)
class title_01(Scene):
    def construct(self):    
        title = Tex("Sección", font_size = 90).shift(UP*1.5)
        number = Tex("1", font_size = 90, color = BLUE).next_to(title, RIGHT).align_to(title, DOWN)
        title_line = VGroup(title, number)
        line = Line([-3.0, 0.0, 0.0], [3.0, 0.0, 0.0], color = YELLOW).next_to(title_line, DOWN)
        subtitle = Tex("Presentación del problema", font_size = 60).next_to(line, DOWN*1.5)
        self.play(AnimationGroup(DrawBorderThenFill(title_line), Create(line), lag_ratio = 0.5, run_time = 2.0))
        self.play(FadeIn(subtitle), run_time = 1.5)
        self.wait(3)