from manim import *
from numpy import *
from utils import *

fs = 28

# Sección 4.8
class manim_10(Scene):
    def construct(self):        
        title = Title("Números Construibles")
        self.play(DrawBorderThenFill(title))

        def_lines = [
            "Un número (real) x es construible si se puede construir",
            "con regla y compás un segmento de su medida"
        ]
        constr_def = write_paragraph(def_lines, font_size=fs, t2c={'construible': BLUE}, font='Arial').shift(UP*2)
        
        segment_group = DoubleArrow(ORIGIN, RIGHT, buff = 0, max_tip_length_to_length_ratio = 0.1)
        segment_left = Line(UP/8, DOWN/8, buff = 0).next_to(segment_group, LEFT, buff = 0)
        segment_right = Line(UP/8, DOWN/8, buff = 0).next_to(segment_group, RIGHT, buff = 0)
        segment_label = Text(r"K", font_size = fs).next_to(segment_group, DOWN)
        segment_group = Group(segment_group, segment_left, segment_right, segment_label).next_to(constr_def, RIGHT).shift(DOWN/4) # sketchy vertical alignment

        set_lines = [
            "El conjunto de los números construibles K incluye a:"
        ]
        constr_set = write_paragraph(set_lines, font_size= fs, t2c={'K': BLUE}, font='Arial').next_to(constr_def, DOWN).align_to(constr_def, LEFT)

        set_elements_lines = [
            r"Los números enteros $\mathbb{Z}$ y racionales $\mathbb{Q}$ e.g. $0, 1, -5, -\frac{2}{3}, \dots$",
            r"Las raíces cuadradas de enteros o racionales e.g. $\sqrt{3}, \sqrt{\frac{2}{3}}, \dots$",
            r"Las sumas, productos y raíces de los anteriores e.g. $\sqrt{1 - \frac{5}{3} + \sqrt{2}}$"
        ]
        set_elements = write_tex_paragraph(set_elements_lines, all_dots = True, font_size = fs, tex_template = TexTemplate().add_to_preamble(r"\usepackage{amssymb}")).next_to(constr_set, DOWN).align_to(constr_def, LEFT).shift(RIGHT/2)
        

        iter_ex_lines = [r"$\sqrt{\sqrt{\sqrt{3} + \sqrt{\sqrt{2}}}}$"]
        iter_ex = write_tex_paragraph(iter_ex_lines, paragraph_dot = False, font_size = fs*1.75, tex_template = TexTemplate().add_to_preamble(r"\usepackage{amssymb}"))
        iter_ex.shift(UP)
        # animaciones
        self.play(Write(constr_def), run_time = 3)
        self.play(FadeIn(segment_group))
        self.wait(3)
        self.play(Write(constr_set), run_time = 3)
        self.wait(3)
        # me cansé del write 3blue1brownero, this is pretty goofy tho
        self.play(FadeIn(set_elements.submobjects[0]), FadeIn(set_elements.submobjects[1]))
        self.play(FadeIn(set_elements.submobjects[2]), FadeIn(set_elements.submobjects[3]))
        self.play(FadeIn(set_elements.submobjects[4]), FadeIn(set_elements.submobjects[5]))
        #self.play(AnimationGroup(*[FadeIn(line) for line in set_elements.submobjects]), lag_ratio = 0.2, run_time = 9) 
        self.wait(6)
        self.play(AnimationGroup(FadeOut(constr_def), FadeOut(segment_group), FadeOut(constr_set), FadeOut(set_elements), lag_ratio = 0.2, run_time = 3))
        self.wait(3)
        self.play(Write(iter_ex), run_time = 3)
        self.wait(3)