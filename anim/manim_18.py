from manim import *
from numpy import *
from utils import *
from manim_rubikscube import *

fs = 40
# Introduction
class manim_18(ThreeDScene):
    def construct(self):
        cube = RubiksCube(
            colors=["#E86D6D", "#FCB07C", "#F7CE9C", "#EDEAD1", "#009698", "#8AD19F"]
        ).scale(0.6).shift(2*LEFT+2*DOWN)
        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state("BUBBBFUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR")

        self.move_camera(phi=50*DEGREES, theta=160*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

        self.add(cube)
        self.wait(3)

         # Rotate the camera around the RubiksCube for 8 seconds
        self.begin_ambient_camera_rotation(rate=0.7)   #0.5

        # Loop through results of the kociemba algorithm
        i = 0
        for m in cube.solve_by_kociemba(state):
            # Execute the move
            if i == 10:
                break
            self.play(CubeMove(cube, m), run_time=0.5)
            i += 1

        for i in range(3):
            self.play(
                Rotating(cube, radians=PI/6, run_time=0.1)
            )
            self.play(
                Rotating(cube, radians=-PI/6, run_time=0.1)
            )

        self.play(Uncreate(cube), run_time=2)

        self.wait()