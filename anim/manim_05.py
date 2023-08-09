from manim import *
from numpy import *

line_thick = DEFAULT_STROKE_WIDTH * 1.5
point_thick = DEFAULT_STROKE_WIDTH * 0.4
aux_thick, aux_arc_len = DEFAULT_STROKE_WIDTH * 0.6, PI/16
fs = 40

# Sección 3.1
class manim_05(Scene):
    def trazar_arco(self, arc: Arc, run_time = 2.0, show_vect = True):
        center, radius, start_angle, angle, color = arc.arc_center, arc.radius, arc.start_angle, arc.angle, arc.color
        if(show_vect):
            vect = Arrow(start = center, end = center + [cos(start_angle) * radius, sin(start_angle) * radius, 0.0], buff = 0, color = color, 
                         stroke_width = aux_thick, max_tip_length_to_length_ratio = 0.05, tip_shape = StealthTip, stroke_opacity = 0.5) 
            self.play(Create(vect), run_time = run_time/8)
            self.play(
                Create(arc),
                Rotate(vect, angle, about_point = center),
                run_time = run_time*6/8
            )
            self.play(Uncreate(vect), run_time = run_time/8)
        else:
            self.play(Create(arc), run_time = run_time)
    
    def construct(self):
        # compilar con --save-sections para generar vídeos separados para cada sección
        
        # puntos base
        pA_coords, pB_coords, pC_coords, pD_coords = [-2.0, -2.0, 0.0], [2.0, 2.0, 0.0], [-2.0, 0.0, 0.0], [2.0, 0.0, 0.0]
        pA = Dot(pA_coords, color = RED, stroke_width = point_thick)
        pA_label = Tex("$A = (A_x, A_y)$", font_size = fs*0.75, color = RED).next_to(pA, DOWN)
        pB = Dot(pB_coords, color = RED, stroke_width = point_thick)
        pB_label = Tex("$B = (B_x, B_y)$", font_size = fs*0.75, color = RED).next_to(pB, UP)
        pC = Dot(pC_coords, color = BLUE, stroke_width = point_thick)
        pC_label = Tex("$C = (C_x, C_y)$", font_size = fs*0.75, color = BLUE).next_to(pC, DOWN)
        pD = Dot(pD_coords, color = BLUE, stroke_width = point_thick)
        pD_label = Tex("$D = (D_x, D_y)$", font_size = fs*0.75, color = BLUE).next_to(pD, DOWN)

        # puntos de interseccion
        pE = Dot([0.0, 0.0, 0.0], color = WHITE, stroke_width = point_thick)
        pE_label = Tex("E", font_size = fs).next_to(pE, DOWN)
        pF = Dot([sqrt(7)-1, sqrt(7)-1, 0.0], color = WHITE, stroke_width = point_thick)
        pF_label = Tex("F", font_size = fs).next_to(pF, RIGHT)
        pG = Dot([6/5, -12/5, 0.0], color = WHITE, stroke_width = point_thick)
        pG_label = Tex("G", font_size = fs).next_to(pG, UP)

        # lineas y rectas
        line1 = Line(pA_coords, pB_coords, buff = 0, color = RED, stroke_width = line_thick)
        line2 = Line(pC_coords, pD_coords, buff = 0, color = BLUE, stroke_width = line_thick)
        circle1 = Arc(arc_center = pC_coords, start_angle = -PI/4, angle = PI/2, radius = 4, stroke_width = line_thick, stroke_color = BLUE)
        circle2 = Arc(arc_center = pB_coords, start_angle = -PI, angle = PI/2, radius = 2*sqrt(5), stroke_width = line_thick, stroke_color = RED)
        
        # dibujar puntos
        self.play(AnimationGroup(FadeIn(pA), FadeIn(pB), FadeIn(pA_label), FadeIn(pB_label), FadeIn(pC), FadeIn(pD), FadeIn(pC_label), FadeIn(pD_label), lag_rate = 0.5))
        self.wait(1)

        # parte 1 : intersección rectas l1 y l2
        self.play(Create(line1))
        self.wait(1)
        self.play(Create(line2))
        self.wait(3)
        
        # ecuaciones
        eq_line1 = Tex(r"$y - A_y = \frac{B_y -  A_y}{B_x - A_x}(x - A_x)$", color = RED, font_size = fs).move_to([-4.5, 3.0, 0.0])
        eq_line2 = Tex(r"$y - C_y = \frac{D_y -  C_y}{D_x - C_x}(x - C_x)$", color = BLUE, font_size = fs).next_to(eq_line1, DOWN).align_to(eq_line1, LEFT)
        self.play(AnimationGroup(FadeIn(eq_line1), FadeIn(eq_line2), lag_rate = 1))
        self.wait(2)
        
        # plugging numbers
        pA_label_plugged = Tex("$A = (-2, -2)$", font_size = fs*0.75, color = RED).next_to(pA, DOWN)
        pB_label_plugged = Tex("$B = (2, 2)$", font_size = fs*0.75, color = RED).next_to(pB, UP)
        pC_label_plugged = Tex("$C = (-2, 0)$", font_size = fs*0.75, color = BLUE).next_to(pC, DOWN)
        pD_label_plugged = Tex("$D = (2, 0)$", font_size = fs*0.75, color = BLUE).next_to(pD, DOWN)
        eq_line1_plugged = Tex(r"$y = x$", color = RED, font_size = fs).align_to(eq_line1, LEFT).align_to(eq_line1, UP)
        eq_line2_plugged = Tex(r"$y = 0$", color = BLUE, font_size = fs).next_to(eq_line1, DOWN).align_to(eq_line1_plugged, LEFT)
        originals = [pA_label, pB_label, pC_label, pD_label, eq_line1, eq_line2]
        plugins = [pA_label_plugged, pB_label_plugged, pC_label_plugged, pD_label_plugged, eq_line1_plugged, eq_line2_plugged]
        eq_group = Group(eq_line1_plugged, eq_line2_plugged)
        self.play(AnimationGroup(*[Transform(originals[i], plugins[i]) for i in range(len(originals))]))
        self.wait(1)

        # intersección
        eq_pE = Tex(r"$\Longrightarrow E = (0, 0)$", color = WHITE, font_size = fs).next_to(eq_group, RIGHT)
        self.play(DrawBorderThenFill(eq_pE))
        self.play(FadeIn(pE), FadeIn(pE_label))
        self.wait(1)
        group1 = Group(line1, line2, eq_line1, eq_line2, eq_line1_plugged, eq_line2_plugged, eq_pE, pE, pE_label)
        self.play(FadeOut(group1))
        
        # parte 2 : intersección recta - circunferencia
        self.next_section()
        self.play(Create(line1))
        self.wait(1)
        self.trazar_arco(circle1)
        self.wait(3)
        
        # ecuaciones
        eq_line1 = Tex(r"$y - A_y = \frac{B_y -  A_y}{B_x - A_x}(x - A_x)$", color = RED, font_size = fs*0.75).move_to([-4.5, 3.0, 0.0])
        eq_circle1 = Tex(r"${(x - C_x)}^2 + {(y - C_y)}^2 = r^2$", color = BLUE, font_size = fs*0.75).next_to(eq_line1, DOWN).align_to(eq_line1, LEFT)
        self.play(AnimationGroup(FadeIn(eq_line1), FadeIn(eq_circle1), lag_rate = 1))
        self.wait(2)

        # plugging numbers
        eq_line1_plugged = Tex(r"$y = x$", color = RED, font_size = fs*0.75).align_to(eq_line1, LEFT).align_to(eq_line1, UP)
        eq_circle1_plugged = Tex(r"${(x + 2)}^2 + y^2 = 16$", color = BLUE, font_size = fs*0.75).next_to(eq_line1, DOWN).align_to(eq_line1_plugged, LEFT)
        originals = [eq_line1, eq_circle1]
        plugins = [eq_line1_plugged, eq_circle1_plugged]
        eq_group = Group(eq_line1_plugged, eq_circle1_plugged)
        self.play(AnimationGroup(*[Transform(originals[i], plugins[i]) for i in range(len(originals))]))
        self.wait(1)

        # intersección
        eq_pF = Tex(r"$\Longrightarrow F = (\sqrt{7}-1, \sqrt{7}-1)$", color = WHITE, font_size = fs*0.75).next_to(eq_group, RIGHT)
        self.play(DrawBorderThenFill(eq_pF))
        self.play(FadeIn(pF), FadeIn(pF_label))
        self.wait(1)
        group2 = Group(line1, circle1, eq_line1, eq_circle1, eq_line1_plugged, eq_circle1_plugged, eq_pF, pF, pF_label, pA, pA_label)
        self.play(FadeOut(group2))
        
        # parte 3 - intersección circunferencia - circunferencia
        self.next_section()
        self.trazar_arco(circle1)
        self.wait(1)
        self.trazar_arco(circle2)
        self.wait(3)
        
        # ecuaciones
        eq_circle1 = Tex(r"${(x - C_x)}^2 + {(y - C_y)}^2 = r_1^2$", color = BLUE, font_size = fs*0.75).move_to([-4.5, 3.0, 0.0])
        eq_circle2 = Tex(r"${(x - B_x)}^2 + {(y - B_y)}^2 = r_2^2$", color = RED, font_size = fs*0.75).next_to(eq_circle1, DOWN).align_to(eq_circle1, LEFT)
        self.play(AnimationGroup(FadeIn(eq_circle1), FadeIn(eq_circle2), lag_rate = 1))
        self.wait(2)

        # plugging numbers
        eq_circle1_plugged = Tex(r"${(x + 2)}^2 + y^2 = 16$", color = BLUE, font_size = fs*0.75).align_to(eq_circle1, LEFT).align_to(eq_circle1, UP)
        eq_circle2_plugged = Tex(r"${(x - 2)}^2 + (y - 2)^2 = 20$", color = RED, font_size = fs*0.75).next_to(eq_circle1, DOWN).align_to(eq_circle1_plugged, LEFT)
        originals = [eq_circle1, eq_circle2]
        plugins = [eq_circle1_plugged, eq_circle2_plugged]
        eq_group = Group(eq_circle1_plugged, eq_circle2_plugged)
        self.play(AnimationGroup(*[Transform(originals[i], plugins[i]) for i in range(len(originals))]))
        self.wait(1)

        # intersección
        eq_pG = Tex(r"$\Longrightarrow G = (\frac{6}{5}, \frac{-12}{5})$", color = WHITE, font_size = fs*0.75).next_to(eq_group, RIGHT)
        self.play(DrawBorderThenFill(eq_pG))
        self.play(FadeIn(pG), FadeIn(pG_label))
        self.wait(3)
        
        # done
        group2 = Group(circle1, circle2, eq_circle1, eq_circle2, eq_circle1_plugged, eq_circle2_plugged, eq_pG, pG, pG_label, pB, pB_label, pC, pC_label, pD, pD_label)
        self.play(FadeOut(group2))