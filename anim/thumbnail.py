from manim import *
from numpy import *
from utils import *
import manimpango

fs = 48


class thumbnail(Scene):
    def construct(self):
        # Change the background color
        self.camera.background_color = "#f2f1e8"
        for r in range(3, 12):
            self.add(Circle(color="#0d698b", radius=r))
            self.add(Square(color="#050533", side_length=2*r))


        # Add the vertical lines of circles and squares
        for h in range(-6, 6):
            for d in [6.5, 4.5]:   # Leaving a gap in the middle
                # Square and circle of the same length/diameter, and a smaller circle inside
                self.add(Circle(color="#0d698b", radius=0.5).shift([-d, h, 0]))
                self.add(Square(color="#050533", side_length=1).shift([-d, h, 0]))
                self.add(Circle(color="#0d698b", radius=0.2).shift([-d, h, 0]))

                self.add(Circle(color="#0d698b", radius=0.2).shift([d, h, 0]))
                self.add(Circle(color="#0d698b", radius=0.5).shift([d, h, 0]))
                self.add(Square(color="#050533", side_length=1).shift([d, h, 0]))

            d = 5.5     # In the gap left by the two previous columns
            if h % 2 == 0:      # Skipping every other row
                continue
            # Three squares of different sizes inscribed in each other
            self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([d, h, 0]))
            self.add(Square(color="#050533", side_length=0.46).shift([d, h, 0]))
            self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([d, h, 0]))


            self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([-d, h, 0]))
            self.add(Square(color="#050533", side_length=0.46).shift([-d, h, 0]))
            self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([-d, h, 0]))


        # Rotated squares at the top, right, bottom and left of the main square and circle
        self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([0, 3.5, 0]))
        self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([3.5, 0, 0]))
        self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([0, -3.5, 0]))
        self.add(Square(color="#050533", side_length=0.707).rotate(PI/4).shift([-3.5, 0, 0]))
        self.add(Square(color="#050533", side_length=0.46).shift([0, 3.5, 0]))
        self.add(Square(color="#050533", side_length=0.46).shift([3.5, 0, 0]))
        self.add(Square(color="#050533", side_length=0.46).shift([0, -3.5, 0]))
        self.add(Square(color="#050533", side_length=0.46).shift([-3.5, 0, 0]))
        self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([0, 3.5, 0]))
        self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([3.5, 0, 0]))
        self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([0, -3.5, 0]))
        self.add(Square(color="#050533", side_length=0.27).rotate(PI/4).shift([-3.5, 0, 0]))


        # Add the title
        title_1 = Text("La", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, 1.8, 0])
        title_2 = Text("cuadratura", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, 0.6, 0])
        title_3 = Text("del", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, -0.6, 0])
        title_4 = Text("círculo", font_size = fs, color = "#FF272A", stroke_width=0.01, font="Augustus").shift([0, -1.8, 0])

        for title in [title_1, title_2, title_3, title_4]:
            title_copy = title.copy()
            title_copy.set_color(GRAY_B)
            title_copy.shift([0.05, -0.05, 0])
            self.add(title_copy)

        self.add(title_1)
        self.add(title_2)
        self.add(title_3)
        self.add(title_4)

        self.wait(2)
