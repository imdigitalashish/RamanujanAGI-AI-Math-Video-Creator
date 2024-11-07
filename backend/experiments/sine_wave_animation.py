from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )

        sine_wave = axes.plot(lambda x: np.sin(x), color=WHITE)
        sine_label = axes.get_graph_label(sine_wave, label='\\sin(x)')

        self.play(Create(axes))
        self.play(Create(sine_wave), Write(sine_label))
        self.wait(2)