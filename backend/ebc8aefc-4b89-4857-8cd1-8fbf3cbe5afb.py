from manim import *

class CircleScene(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        self.play(Create(circle))  # Draw the circle on screen
        self.wait(2)  # Wait for 2 seconds before ending the scene