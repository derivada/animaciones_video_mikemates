from manim import *
from numpy import *

# Sección 3.1
class manim_02(Scene):
    def construct(self):
        # constantes para retocar más fácil
        rect_h, rect_w = 1, 2
        rect_color, rect_thick, rect_fill, rect_fill_opacity = RED, DEFAULT_STROKE_WIDTH * 1.2, RED_D, 0.5
        arc_color, arc_thick, arc_alpha = GREEN, DEFAULT_STROKE_WIDTH, 0.5
        aux_color, aux_thick, aux_arc_len = BLUE, DEFAULT_STROKE_WIDTH * 0.6, PI/16
        point_color, point_thick = WHITE, DEFAULT_STROKE_WIDTH * 0.6
        cuad_color, cuad_color_highlight, cuad_thick, cuad_fill, cuad_fill_opacity = YELLOW, WHITE, DEFAULT_STROKE_WIDTH * 1.2, YELLOW_D, 0.5
        fs = 32
        removeGroup = Group() # cosas que se quitan al final

        # rectángulo
        rect = Rectangle(rect_color, rect_h, rect_w, stroke_width = rect_thick)
        pB = Dot([-rect_w /2, rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pB_label = Tex("B", font_size = fs).next_to(pB, UL / 2)
        pC = Dot([-rect_w /2, -rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pC_label = Tex("C", font_size = fs).next_to(pC, DL / 2)
        pD = Dot([rect_w /2, -rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pD_label = Tex("D", font_size = fs).next_to(pD, DR / 2)
        pE = Dot([rect_w /2, rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pE_label = Tex("E", font_size = fs).next_to(pE, UR / 2)
        self.play(Create(rect))
        self.play(AnimationGroup(FadeIn(pB), FadeIn(pB_label), FadeIn(pC), FadeIn(pC_label), FadeIn(pD), FadeIn(pD_label), FadeIn(pE), FadeIn(pE_label), lag_ratio = 0.25))
        removeGroup.add(pB, pB_label, pC, pC_label, pD, pD_label, pE, pE_label)
        self.wait(3)

        # arco DF
        pF = Dot([rect_w /2 + rect_h, rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pF_label = Tex("F", font_size = fs).next_to(pF, DR / 2)
        arc_df = ArcBetweenPoints(pD.get_center(), pF.get_center(), stroke_width = arc_thick, stroke_color = arc_color, stroke_opacity = arc_alpha)
        self.play(Create(arc_df))
        self.play(FadeIn(pF), FadeIn(pF_label))
        removeGroup.add(pF, pF_label, arc_df)
        self.wait(3)

        # construccion mediatriz (opcional)
        arc_bf_up = Arc(rect_w + rect_h, PI/3 - aux_arc_len/2, aux_arc_len, arc_center = pB.get_center(), color = aux_color, stroke_width = aux_thick)
        arc_bf_down = Arc(rect_w + rect_h, -PI/3 - aux_arc_len/2, aux_arc_len, arc_center = pB.get_center(), color = aux_color, stroke_width = aux_thick)
        arc_fb_up = Arc(rect_w + rect_h, 2*PI/3 - aux_arc_len/2, aux_arc_len, arc_center = pF.get_center(), color = aux_color, stroke_width = aux_thick)
        arc_fb_down = Arc(rect_w + rect_h, -2*PI/3 - aux_arc_len/2, aux_arc_len, arc_center = pF.get_center(), color = aux_color, stroke_width = aux_thick)
        midline = DashedLine(start = [rect_h/2, rect_w + rect_h + 0.5, 0.0], end = [rect_h/2, - rect_w - rect_h - 0.5, 0.0], color = aux_color, stroke_width = aux_thick) 
        pG = Dot([rect_h/2, rect_h/2, 0.0], color = point_color, stroke_width = point_thick)
        pG_label = Tex("G", font_size = fs).next_to(pG, UP / 2)
        self.play(AnimationGroup(Create(arc_bf_up), Create(arc_fb_up), lag_ratio = 0.5))
        self.play(AnimationGroup(Create(arc_bf_down), Create(arc_fb_down), lag_ratio = 0.5))
        self.wait(1)
        self.play(AnimationGroup(Create(midline), FadeIn(pG), FadeIn(pG_label), lag_ratio = 1))
        self.play(FadeOut(arc_bf_up), FadeOut(arc_bf_down), FadeOut(arc_fb_up), FadeOut(arc_fb_down), FadeOut(midline)) # quitar clutter
        removeGroup.add(pG, pG_label)
        self.wait(3)

        # circulo G y triangulo GEH
        sq_size = sqrt(rect_h*rect_w)
        circle = Circle(rect_w/2 + rect_h/2, arc_center = pG.get_center(), color = arc_color, stroke_width = arc_thick, stroke_opacity = arc_alpha)
        pH = Dot([rect_w/2, rect_h/2 + sq_size, 0.0], color = point_color, stroke_width = point_thick)
        pH_label = Tex("H", font_size = fs).next_to(pH, UP / 2)
        eh = Line(pE.get_center(), pH.get_center(), color = cuad_color, stroke_width = cuad_thick)
        self.play(Create(circle))
        self.play(Create(eh)) 
        self.bring_to_back(eh) # maybe needs fix
        self.play(FadeIn(pH), FadeIn(pH_label))
        removeGroup.add(pH, pH_label, circle)
        self.wait(3)

        # construir cuadrado
        cuad = Polygon(pE.get_center(), pH.get_center(), pH.get_center() + [sq_size, 0.0, 0.0], pE.get_center() + [sq_size, 0.0, 0.0], color = cuad_color, stroke_width = cuad_thick)
        self.play(Create(cuad))
        self.bring_to_back(cuad) # maybe needs fix
        self.remove(eh)
        self.wait(2)
        self.play(Indicate(cuad, scale_factor = 1.05, run_time = 1.0, color = cuad_color_highlight))
        self.wait(3)

        # quitar todo excepto rect y sq, resaltar áreas y números
        self.play(AnimationGroup(*[FadeOut(s) for s in removeGroup], lag_ratio = 0.1))
        equal = Tex("=", font_size = fs*4)
        finalGroup = Group(rect, equal, cuad)
        self.play(rect.animate.set_fill(rect_fill, rect_fill_opacity), cuad.animate.set_fill(cuad_fill, cuad_fill_opacity))
        self.play(FadeIn(equal), finalGroup.animate.arrange(direction = RIGHT, buff = 0.5))
        self.wait(3)