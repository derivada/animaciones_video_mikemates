from manim import *
from numpy import *
from utils import *

fs = 48

class thumbnail_clip_end(Scene):
    def construct(self):
        agradecimiento = Tex("Gracias por ver el vídeo!", color = GREEN_A, font_size = fs).shift(UP*2)

        self.play(Write(agradecimiento), run_time = 2.5)
        self.play(ShowPassingFlash(Underline(agradecimiento), time_width = 0.3), run_time = 2)


        twitter_1 = Tex("Síguenos en ", font_size = fs)
        twitter_2 = Tex("X", color = LIGHT_GRAY, font_size = fs).next_to(twitter_1)
        twitter_line = VGroup(twitter_1, twitter_2).align_to(ORIGIN).shift(LEFT)
        twitter_2_real = Tex("Twitter", color = "#0084b4", font_size = fs).next_to(twitter_1)
        twitter_xiana = Tex("@Kinai24", font_size = fs*0.9).next_to(twitter_line, DOWN*2).shift(LEFT*0.5)
        twitter_pablo = Tex("@tntpablo", font_size = fs*0.9).next_to(twitter_line, DOWN*2).shift(RIGHT*1.75)
        
        self.play(Write(twitter_line), run_time = 1.5)
        self.play(FadeIn(twitter_xiana), FadeIn(twitter_pablo))
        self.wait(2)
        cross = Cross(twitter_2, scale_factor = 1.1, color = PURE_RED)
        self.play(Create(cross), run_time = 1.5)
        self.wait(0.5)
        self.play(Transform(twitter_2, twitter_2_real), FadeOut(cross), run_time = 1.5)
        self.remove(twitter_2_real)
        self.play(Indicate(twitter_2, color = "#00aced", scale_factor = 1.1), run_time = 2)
        self.wait(2)

        