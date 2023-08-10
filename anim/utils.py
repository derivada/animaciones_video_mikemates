from manim import *
from numpy  import *

def trazar_arco(scene: Scene, arc: Arc, run_time = 2.0, show_vect = True):
    center, radius, start_angle, angle, color = arc.arc_center, arc.radius, arc.start_angle, arc.angle, arc.color
    if(show_vect):
        vect = Arrow(start = center, end = [center[0] + cos(start_angle) * radius, center[1] + sin(start_angle) * radius, center[2]], buff = DEFAULT_DOT_RADIUS, color = color, 
                    max_tip_length_to_length_ratio = 0.05, tip_shape = StealthTip, stroke_opacity = 0.5, fill_opacity = 0.5, stroke_width = DEFAULT_STROKE_WIDTH * 0.66) 
        scene.play(Create(vect), run_time = run_time/8)
        scene.play(
            Create(arc),
            Rotate(vect, angle, about_point = center),
            run_time = run_time*6/8
        )
        scene.play(FadeOut(vect), run_time = run_time/8)
    else:
        scene.play(Create(arc), run_time = run_time)