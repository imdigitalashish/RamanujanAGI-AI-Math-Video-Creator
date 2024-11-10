from manim import *

class CircleAndSquare(Scene):
    def construct(self):
        circle = Circle()           # Create a circle
        square = Square()           # Create a square

        # Position the square next to the circle
        square.next_to(circle, RIGHT, buff=0.5)

        # Add both shapes to the scene
        self.play(Create(circle), Create(square))
        self.wait(2)