from manim import *

class SquareScene(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait(1)