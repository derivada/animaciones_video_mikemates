from manim import *
from numpy import *
from utils import *

fs = 60
poly_points = [[2.0, 0.0, 0.0], [2.0, 2.5, 0.0], [-3.0, 3.0, 0.0], [-1.5, 0.5, 0.0], [-2.0, -3.0, 0.0], [3.0, -2.0, 0.0]]
poly_color, triang_line_color = BLUE, WHITE


# Sección 3.3.1-3.3.4
class manim_03(Scene):
    def construct(self):
        poly = Polygon(*poly_points, color=poly_color, stroke_width = DEFAULT_STROKE_WIDTH*1.5)
        self.play(Create(poly), run_time = 2)
        self.wait(3)
        triang_line_1 = Line(poly_points[0], poly_points[4], color=triang_line_color, buff = DEFAULT_STROKE_WIDTH)
        triang_line_2 = Line(poly_points[4], poly_points[1], color=triang_line_color, buff = DEFAULT_STROKE_WIDTH)
        triang_line_3 = Line(poly_points[1], poly_points[3], color=triang_line_color, buff = DEFAULT_STROKE_WIDTH)
        self.play(Create(triang_line_1))
        self.wait(0.3)
        self.play(Create(triang_line_2))
        self.wait(0.3)
        self.play(Create(triang_line_3))
        self.wait(3)

        poly_group = VGroup(poly, triang_line_1, triang_line_2, triang_line_3)

        triangle_1 = Polygon(poly_points[0], poly_points[5], poly_points[4], color = PURPLE_A, fill_opacity = 0.5, stroke_width = 0)
        triangle_2 = Polygon(poly_points[0], poly_points[4], poly_points[1], color = PURPLE_B, fill_opacity = 0.5, stroke_width = 0)
        triangle_3 = Polygon(poly_points[1], poly_points[4], poly_points[3], color = PURPLE_C, fill_opacity = 0.5, stroke_width = 0)
        triangle_4 = Polygon(poly_points[1], poly_points[3], poly_points[2], color = PURPLE_D, fill_opacity = 0.5, stroke_width = 0)
        triang_group = VGroup(triangle_1, triangle_2, triangle_3, triangle_4)
        self.play(AnimationGroup(FadeIn(triangle_1), FadeIn(triangle_2), FadeIn(triangle_3), FadeIn(triangle_4), run_time = 3, lag_ratio = 0.8))
        self.play(triangle_1.animate.shift(RIGHT * 1.5),
                    triangle_2.animate.shift(UR),
                    triangle_3.animate.shift(DOWN * 0.8 + LEFT*1.5),
                    triangle_4.animate.shift(LEFT),
                    FadeOut(poly_group, run_time =1))
        self.wait(3)

        self.play(*[triangle.animate.scale(0.5) for triangle in triang_group])
        self.play(triang_group.animate.arrange(LEFT))
        self.wait(3)
        
        for tri in triang_group:
            vert = tri.get_vertices()
            side_len = sqrt(abs(0.5 * (vert[0][0] * (vert[1][1]-vert[2][1]) + vert[1][0] * (vert[2][1]-vert[0][1]) + vert[2][0] * (vert[0][1] - vert[1][1]))))
            quad = Square(side_len, color = tri.get_color(), fill_opacity = 0.5,  stroke_width = 0).move_to(tri.get_center()) 
            self.play(Transform(tri, quad))
            self.wait(0.5)
        
        self.wait(1)
        self.play(triang_group.animate.arrange(DOWN))
        self.play(triang_group.animate.shift(RIGHT*4))
        self.wait(3)

        pitagoras_pos = [-3.5, 3.0, 0.0]
        pitagoras = Tex("Teorema de Pitágoras", font_size = fs).move_to(pitagoras_pos)
        pitagoras_points = [[1.5, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
        pitagoras_triang = Polygon(*pitagoras_points)
        label_a = Tex("a").next_to(pitagoras_triang, DOWN)
        label_b = Tex("b").next_to(pitagoras_triang, LEFT)
        label_c = Tex("c").move_to(pitagoras_triang, RIGHT/4).shift(UL/4)
        pitagoras_geom = VGroup(pitagoras_triang, label_a, label_b, label_c).next_to(pitagoras, DOWN).align_to(pitagoras, LEFT)
        pitagoras_eq = Tex("$a^2 + b^2 = c^2$", font_size = fs, color = BLUE).next_to(pitagoras_geom, RIGHT*1.25).shift(UP/4)
        self.play(DrawBorderThenFill(pitagoras), run_time = 2)
        self.play(FadeIn(pitagoras_geom))
        self.play(DrawBorderThenFill(pitagoras_eq), run_time = 2)
        self.wait(3)

        # down-left corner of the construction triangle
        constr_corner = [-3.5, -2.0, 0.0]
        # first 2
        self.play(triang_group[0].animate.next_to(constr_corner, UL, buff = 0), triang_group[1].animate.next_to(constr_corner, DR, buff = 0), run_time = 2)
        self.wait(2)
        right_p, up_p = triang_group[1].get_boundary_point(UR), triang_group[0].get_boundary_point(UR)
        triangle_add_2 = Polygon(right_p, constr_corner, up_p, color = YELLOW_B, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(triangle_add_2))
        hyp = right_p - up_p
        perp = [-hyp[1], hyp[0], 0.0]
        square_add_2 = Polygon(right_p, up_p, up_p + perp, right_p + perp, color = BLUE_B, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(square_add_2))
        self.wait(2)
        self.play(AnimationGroup(
                    square_add_2.animate.rotate(angle = arctan((np.linalg.norm(up_p - constr_corner)) / np.linalg.norm((constr_corner - right_p))), about_point = right_p),
                    FadeOut(triang_group[0]), FadeOut(triang_group[1]), FadeOut(triangle_add_2), lag_ratio = 0.2, run_time = 2))
        
        # next 2
        self.play(square_add_2.animate.next_to(constr_corner, UL, buff = 0), triang_group[2].animate.next_to(constr_corner, DR, buff = 0), run_time = 2)
        self.wait(2)
        right_p, up_p = triang_group[2].get_boundary_point(UR), square_add_2.get_boundary_point(UR)
        triangle_add_3 = Polygon(right_p, constr_corner, up_p, color = YELLOW_C, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(triangle_add_3))
        hyp = right_p - up_p
        perp = [-hyp[1], hyp[0], 0.0]
        square_add_3 = Polygon(right_p, up_p, up_p + perp, right_p + perp, color = BLUE_C, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(square_add_3))
        self.wait(2)
        self.play(AnimationGroup(
                    square_add_3.animate.rotate(angle = arctan((np.linalg.norm(up_p - constr_corner)) / np.linalg.norm((constr_corner - right_p))), about_point = right_p),
                    FadeOut(square_add_2), FadeOut(triang_group[2]), FadeOut(triangle_add_3), lag_ratio = 0.2, run_time = 2))
        self.wait(2)

        # last 2
        self.play(square_add_3.animate.next_to(constr_corner, UL, buff = 0), triang_group[3].animate.next_to(constr_corner, DR, buff = 0), run_time = 2)
        self.wait(2)
        right_p, up_p = triang_group[3].get_boundary_point(UR), square_add_3.get_boundary_point(UR)
        triangle_add_4 = Polygon(right_p, constr_corner, up_p, color = YELLOW_D, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(triangle_add_4))
        hyp = right_p - up_p
        perp = [-hyp[1], hyp[0], 0.0]
        square_add_4 = Polygon(right_p, up_p, up_p + perp, right_p + perp, color = BLUE_D, fill_opacity = 0.5, stroke_width = 0)
        self.play(FadeIn(square_add_4))
        self.wait(2)
        self.play(AnimationGroup(
                    square_add_4.animate.rotate(angle = arctan((np.linalg.norm(up_p - constr_corner)) / np.linalg.norm((constr_corner - right_p))), about_point = right_p),
                    FadeOut(square_add_3), FadeOut(triang_group[3]), FadeOut(triangle_add_4), lag_ratio = 0.2, run_time = 2))
        self.wait(2)

        # done
        poly = Polygon(*poly_points, color = BLUE_D, fill_opacity = 0.5, stroke_width = 0).move_to([3.0, 0.0, 0.0]).scale(0.5)
        equal = Tex("=", font_size = fs*1.75)
        self.play(AnimationGroup(FadeOut(pitagoras), FadeOut(pitagoras_geom), FadeOut(pitagoras_eq), lag_ratio = 0.2, run_time = 1))
        self.play(AnimationGroup(square_add_4.animate.move_to([-3.0, 0.0, 0.0]), FadeIn(poly), FadeIn(equal), lag_ratio = 0.8, run_time = 3))
        self.wait(3)