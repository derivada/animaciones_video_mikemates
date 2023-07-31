from manim import *
from numpy import *

# Sección 2.3
class manim_01(Scene):
    def construct(self):
        circle_color = GREEN
        sq_color = RED
        fs = 40 # font size

        circle = Circle(radius = 1.0, color = circle_color)
        self.play(Create(circle))
        self.wait(1)

        sq_size = ValueTracker(1) # value tracker para poder animar cambios de tamaño en texto y cuadrado
        sq = Square(1, color = sq_color, fill_opacity = 0.3)
        sq.add_updater(lambda sq: sq.become(Square(sq_size.get_value(), color = RED, fill_opacity = 0.3))) # usar become para transformar fácil en este caso
        self.play(DrawBorderThenFill(sq))
        self.wait(1)

        # textos
        circle_text = Tex(r"Área del círculo =  ", font_size = fs, color = circle_color)
        sq_text = Tex(r"Área del cuadrado = ", font_size = fs, color = sq_color).next_to(circle_text, DOWN).align_to(circle_text, LEFT)
        circle_text_area = DecimalNumber(3.1415, num_decimal_places=4, font_size = fs, color = circle_color, show_ellipsis=True).next_to(circle_text, RIGHT).align_to(circle_text, DOWN)
        sq_text_area = DecimalNumber(1, font_size = fs, color = sq_color).next_to(sq_text, RIGHT).align_to(sq_text, DOWN)
        sq_text_area.add_updater(lambda mob: mob.set_value(sq_size.get_value() * sq_size.get_value()))
        area_group = VGroup(circle_text, sq_text, circle_text_area, sq_text_area).shift([3.0, 3.0, 0.0])
        self.play(FadeIn(area_group))
        self.wait(1)

        # tweakear para adaptar a la narración
        self.play(sq_size.animate.set_value(2))
        self.wait(1)
        self.play(sq_size.animate.set_value(sqrt(2)))
        self.wait(1)
        self.play(sq_size.animate.set_value(1.75))
        self.wait(3)