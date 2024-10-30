from manim import *

class PairOfLines(Scene):
    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )

        # Create lines
        line1 = Line(start=axes.c2p(-2, -2), end=axes.c2p(2, 2), color=RED)
        line2 = Line(start=axes.c2p(-2, 2), end=axes.c2p(2, -2), color=GREEN)

        # Add axes and lines to the scene
        self.add(axes, line1, line2)

        # Add labels for lines
        line1_label = MathTex("y = x").next_to(line1, UP)
        line2_label = MathTex("y = -x").next_to(line2, DOWN)

        self.add(line1_label, line2_label)

        # Show the scene
        self.wait(2)