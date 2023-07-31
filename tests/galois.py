from manim import *


class Galois(Scene):
    def construct(self):
        title = Title('Fundamental Theorem of Galois Theory')
        self.play(DrawBorderThenFill(title))
        self.wait(1)
        coords_left = [-3.5, 2.0, 0.0]
        coords_right = [3.5, 2.0, 0.0]
        buff = 0.25

        left_rect = RoundedRectangle(corner_radius = 0.5, height = 1.0, width = 2.0).shift(coords_left)
        right_rect = RoundedRectangle(corner_radius = 0.5, height = 1.0, width = 2.0).shift(coords_right)
        self.play(FadeIn(left_rect), FadeIn(right_rect))

        left = Tex(r"Subgroups \\ $H \leq G(E \mid F)$", font_size = 16).shift(coords_left)
        right = Tex(r"Intermediate Fields \\ $F \subseteq K \subseteq E$", font_size = 16).shift(coords_right)
        self.play(FadeIn(left), FadeIn(right))
        self.wait(1)
        
        arrow = DoubleArrow(buff = buff, start = left_rect.get_right(), end = right_rect.get_left(), max_stroke_width_to_length_ratio = 1.5, max_tip_length_to_length_ratio = 0.05)
        self.play(FadeIn(arrow))
        self.wait(1)

        coords_left[1] -= 1.0; coords_right[1] -= 1.0
        left2 = Tex(r"$H$", font_size = 24, color = RED).move_to(coords_left, RIGHT)
        right2 = Tex(r"$E_H$", font_size = 24, color = RED).move_to(coords_right, LEFT)
        arrow2 = Arrow(buff = buff, start = coords_left, end = coords_right, color = RED_D, max_stroke_width_to_length_ratio = 0.5, max_tip_length_to_length_ratio = 0.03)
        self.play(FadeIn(left2), FadeIn(right2), FadeIn(arrow2))

        self.wait(1)

        coords_left[1] -= 0.5; coords_right[1] -= 0.5

        left3 = Tex(r"$G(E \mid K)$", font_size = 24, color = BLUE).move_to(coords_left, RIGHT)
        right3 = Tex(r"$K$", font_size = 24, color = BLUE).move_to(coords_right, LEFT)
        arrow3 = Arrow(buff = buff, start = coords_right, end = coords_left, color = BLUE_D, max_stroke_width_to_length_ratio = 0.5, max_tip_length_to_length_ratio = 0.03)
        self.play(FadeIn(left3), FadeIn(right3), FadeIn(arrow3))

        self.wait(1)

        coords_left[0] -= 1.5
        coords_left[1] -= 1.0
        left4 = Tex(r"The Galois Correspondence:", font_size = 20, color = GREEN).move_to(coords_left, LEFT)
        coords_left[1] -= 0.75
        left5 = Tex(r"""\begin{enumerate}
            \item $K = E_{G(E \mid K)}$
            \item $H = G(E \mid E_H)$
            \item $[E : K] = \lvert G(E \mid K) \rvert$ and $ [K : F] = \frac{\lvert G(E \mid F) \rvert}{\lvert G(E \mid K) \rvert}$
        \end{enumerate}""", font_size = 18).move_to(coords_left, LEFT)
        self.play(DrawBorderThenFill(left4))
        self.wait(0.5)
        self.play(FadeIn(left5))
        self.wait(3)
        coords_right[0] = left5.get_right()[0] + 0.5
        coords_right[1] -= 1.0
        left4 = Tex(r"Relation between normal field extensions and normal groups:", font_size = 20, color = YELLOW).move_to(coords_right, LEFT)
        coords_right[1] -= 0.75
        left5 = Tex(r"""\begin{enumerate}
            \setcounter{enumi}{3}
            \item If $G(E \mid K) \unlhd G(E \mid F)$, then $\forall \sigma \in G(E\mid F)$ we have $\sigma (K) = K$
            \item $G(E \mid K) \unlhd G(E \mid F) \Longleftrightarrow F \subset K$ is normal
            \item If $F \subset K$ is normal, then $G(K \mid F) \cong \frac{G(E \mid F)}{G(E \mid K)}$
        \end{enumerate}""", font_size = 18).move_to(coords_right, LEFT)
        self.play(DrawBorderThenFill(left4))
        self.wait(0.5)
        self.play(FadeIn(left5))
        self.wait(3)
