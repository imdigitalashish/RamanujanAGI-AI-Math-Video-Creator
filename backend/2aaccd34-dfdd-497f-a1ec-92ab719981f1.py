from manim import *

class CircleAndParabola(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        
        # Create a parabola
        parabola = FunctionGraph(lambda x: x**2 - 2, x_range=[-2, 2], color=RED)
        self.play(Create(parabola))
        
        self.wait()