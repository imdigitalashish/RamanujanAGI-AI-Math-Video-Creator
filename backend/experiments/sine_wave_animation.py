```python
from manim import *

class CreateRectangle(Scene):
    def construct(self):
        rectangle = Rectangle(width=4.0, height=2.0)
        self.play(Create(rectangle))
        self.wait()
```