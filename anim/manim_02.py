from manim import *
from numpy import *

circle_color = BLUE
poly_color = RED
fs = 40

# Sección 3.1
class manim_02(Scene):
    def construct(self):

        circle = RegularPolygon(3, color = circle_color)
        self.play(Create(circle), run_time = 2)
        self.wait(2)
        for i in range(4, 10):
            circle_new = RegularPolygon(i, color = circle_color)
            self.remove(circle)
            if not i%6: circle_new.rotate(PI/i)
            self.add(circle_new)
            circle = circle_new
            self.wait(1.5/i)

        for i in range(10, 100, 2):
            circle_new = RegularPolygon(i, color = circle_color)
            self.remove(circle)
            if not i%2: circle_new.rotate(PI/2)
            self.add(circle_new)
            circle = circle_new   
            self.wait(1.5/i)

             
        self.play(Indicate(circle, color = YELLOW), run_time = 2)
        self.wait(2)
        
        circle_text = Tex(r"$\infty$ lados", font_size = fs, color = circle_color).shift([-2.5, -2.0, 0.0])
        self.play(circle.animate.shift([-2.5, 0.0, 0.0]), FadeIn(circle_text))
        self.wait(2)
        
        poly = Polygon([1.5, 0, 0], [1.0, 1.0, 0.0], [0.3, 0.5, 0.0], [-1.0, 1.2, 0.0], [-1.0, -1.2, 0.0], [0.3, -1.0, 0.0], [0.7, 0.6, 0.0], color = poly_color)
        poly.shift([2.5, 0.0, 0.0])
        poly_text1 = Tex(r"$7$ lados", font_size = fs, color = poly_color).shift([2.5, -2.0, 0.0])
        self.play(Create(poly), FadeIn(poly_text1))    
        self.wait(2)

        pointer = Vector(DOWN, color = YELLOW).shift([2.5, 2.75, 0.0])
        pointer_text = Text("¿Podemos cuadrarlo siempre?", font = 'Arial', font_size = fs-18, color = YELLOW).next_to(pointer, UP, buff = 0.1)
        self.play(FadeIn(pointer), DrawBorderThenFill(pointer_text), run_time = 2)
        self.wait(2)

        # transformar a otros poligonos para hacerlo más chulo idk
        poly_text2 = Tex(r"$7$ lados", font_size = fs, color = GREEN).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(RegularPolygon(7, color = GREEN).shift([2.5, 0.0, 0.0])),
                  FadeOut(poly_text1), FadeIn(poly_text2))
        self.wait(0.5)
        poly_text3 = Tex(r"$5$ lados", font_size = fs, color = ORANGE).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(Polygon([1.5, 0.1, 0], [-0.1, 1.6, 0.0], [-1.2, 0.3, 0.0], [-0.2, -1.3, 0.0], [0.5, 0.4, 0.0], color = ORANGE).shift([2.5, 0.0, 0.0])), 
                FadeOut(poly_text2), FadeIn(poly_text3))
        self.wait(0.5)
        poly_text4 = Tex(r"$13$ lados", font_size = fs, color = PURPLE).shift([2.5, -2.0, 0.0])
        self.play(poly.animate.become(RegularPolygon(13, color = PURPLE).shift([2.5, 0.0, 0.0])),
                FadeOut(poly_text3),FadeIn(poly_text4))
        self.wait(2)

        # parte 2 en 3.4
        pointer_text_si = Text("SÍ", font = 'Arial', font_size = fs, color = GREEN).next_to(pointer_text, RIGHT).shift([0.0, 0.1, 0.0])
        self.play(FadeIn(pointer_text_si))
        self.wait(1)

        poly_to_circle = DashedLine(start = [1.25, 0.0, 0.0], end = [-1.25, 0.0, 0.0], color = LIGHTER_GRAY).add_tip(ArrowTriangleTip(fill_opacity = 1, color = LIGHTER_GRAY, width = DEFAULT_ARROW_TIP_LENGTH/2.5))
        quest = Text("???", font = 'Arial', font_size = fs-18, color = LIGHTER_GRAY).next_to(poly_to_circle, UP)

        self.play(AnimationGroup(Create(poly_to_circle), DrawBorderThenFill(quest), lag_ratio = 0.5, run_time = 2))
        self.wait(3)
