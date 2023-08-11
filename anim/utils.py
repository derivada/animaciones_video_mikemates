from manim import *
from numpy import *

def mostrar_grid(scene: Scene):
    grid = NumberPlane(
        background_line_style={
            "stroke_color": GRAY_B,
            "stroke_width": DEFAULT_STROKE_WIDTH * 0.6,
            "stroke_opacity":  0.3
        },
        axis_config={"include_numbers": True}
    )
    scene.add(grid)

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

def write_paragraph(lines, line_spacing: int = 0.2, paragraph_dot: bool = True, all_dots: bool = False, **kwargs) -> VGroup:
    # lines es un array de strings, admite argumentos adicionales del constructor de Text()
    # devuelve el objeto de texto en forma de VGroup
    text = VGroup()
    for line in lines:
        text_line = Text(line, **kwargs)
        if text: # lineas normales
            text_line.next_to(text[-1], DOWN, aligned_edge=LEFT, buff=line_spacing)
            if(all_dots): 
                text.add(Dot().next_to(text_line, LEFT)) 
        elif(paragraph_dot | all_dots): # primera linea y queremos paragraph dot
            text.add(Dot().next_to(text_line, LEFT)) 
        text.add(text_line)
    return text

def write_tex_paragraph(lines, line_spacing: int = 0.2, paragraph_dot: bool = True, all_dots: bool = False, **kwargs) -> VGroup:
    # lines es un array de strings, admite argumentos adicionales del constructor de Tex()
    # devuelve el objeto de texto en forma de VGroup
    text = VGroup()
    for line in lines:
        text_line = Tex(line, **kwargs)
        if text: # lineas normales
            text_line.next_to(text[-1], DOWN, aligned_edge=LEFT, buff=line_spacing)
            if(all_dots): 
                text.add(Dot().next_to(text_line, LEFT)) 
        elif(paragraph_dot | all_dots): # primera linea y queremos paragraph dot
            text.add(Dot().next_to(text_line, LEFT)) 
        text.add(text_line)
    return text