from manim import *

class CreateSquare(Scene):
    def construct(self):
        square = Square()  # Create a square
        self.play(Create(square))  # Show the square on the screen
        self.wait(1)  # Wait for a moment to view the square