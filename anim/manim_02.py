from manim import *
from numpy import *

# Sección 3.1
class manim_02(Scene):
    def construct(self):
        circle_color = GREEN
        poly_color = RED
        fs = 40 # font size

        circle = Circle(radius = 1.0, color = circle_color)
        self.play(Create(circle))
        self.wait(2)
        
        circle_text = Tex(r"$\infty$ lados", font_size = fs, color = circle_color).shift([-2.5, -2.0, 0.0])
        self.play(circle.animate.shift([-2.5, 0.0, 0.0]), FadeIn(circle_text))
        self.wait(2)
        
        poly = Polygon([1.5, 0, 0], [1.0, 1.0, 0.0], [0.3, 0.5, 0.0], [-1.0, 1.2, 0.0], [-1.0, -1.2, 0.0], [0.3, -1.0, 0.0], [0.7, 0.6, 0.0], color = poly_color)
        poly.shift([2.5, 0.0, 0.0])
        poly_text1 = Tex(r"$7$ lados", font_size = fs, color = poly_color).shift([2.5, -2.0, 0.0])
        self.play(Create(poly), FadeIn(poly_text1))    
        self.wait(2)

        pointer = Vector(DOWN).shift([2.5, 2.75, 0.0])
        pointer_text = Text("¿Podemos cuadrarlo siempre?", font = 'Arial', font_size = fs-18).next_to(pointer, UP, buff = 0.1)
        self.play(FadeIn(pointer), DrawBorderThenFill(pointer_text), run_time = 2)
        self.wait(2)

        # transformar a otros poligonos para hacerlo más chulo idk
        poly_text2 = Tex(r"$7$ lados", font_size = fs, color = BLUE).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(RegularPolygon(7, color = BLUE).shift([2.5, 0.0, 0.0])),
                  FadeOut(poly_text1), FadeIn(poly_text2))
        self.wait(0.5)
        poly_text3 = Tex(r"$5$ lados", font_size = fs, color = YELLOW).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(Polygon([1.5, 0.1, 0], [-0.1, 1.6, 0.0], [-1.2, 0.3, 0.0], [-0.2, -1.3, 0.0], [0.5, 0.4, 0.0], color = YELLOW).shift([2.5, 0.0, 0.0])), 
                FadeOut(poly_text2), FadeIn(poly_text3))
        self.wait(0.5)
        poly_text4 = Tex(r"$13$ lados", font_size = fs, color = ORANGE).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(RegularPolygon(13, color = ORANGE).shift([2.5, 0.0, 0.0])),
                FadeOut(poly_text3),FadeIn(poly_text4))
        self.wait(2)
