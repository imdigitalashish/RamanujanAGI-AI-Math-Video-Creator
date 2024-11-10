from manim import *

class PermutationCombination(Scene):
    def construct(self):
        title = Text("Permutations and Combinations", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Permutation Explanation
        perm_text = Text("Permutations: Arrangements of objects", font_size=36)
        perm_text.next_to(title, DOWN)
        self.play(Write(perm_text))
        self.wait(2)

        # Define objects and their arrangement for Permutations
        objects_perm = VGroup(*[Square(side_length=0.5) for _ in range(3)])
        objects_perm.arrange(RIGHT, buff=0.5)
        self.play(FadeIn(objects_perm))
        self.wait(1)
        
        perm_instructions = Text("Total Permutations: 3! = 6", font_size=30)
        perm_instructions.to_edge(DOWN)
        self.play(Write(perm_instructions))
        self.wait(2)

        # Show Permutation Arrangements
        self.play(objects_perm.animate.arrange(RIGHT, buff=0.5).shift(UP))
        for i in range(1, 7):
            self.play(objects_perm.animate.shift(UP * 1.5))
            self.wait(0.5)

        self.play(objects_perm.animate.fade(0.5))
        self.play(FadeOut(perm_text), FadeOut(perm_instructions))

        # Combination Explanation
        comb_text = Text("Combinations: Selections of objects", font_size=36)
        self.play(Write(comb_text))
        self.wait(2)

        # Define objects and their arrangement for Combinations
        objects_comb = VGroup(*[Circle(radius=0.25) for _ in range(3)])
        objects_comb.arrange(RIGHT, buff=0.5)
        self.play(FadeIn(objects_comb))
        self.wait(1)
        
        comb_instructions = Text("Total Combinations: C(3, 2) = 3", font_size=30)
        comb_instructions.to_edge(DOWN)
        self.play(Write(comb_instructions))
        self.wait(2)

        # Show Combination Selection
        self.play(objects_comb[0].animate.set_fill(RED, opacity=0.5), 
                  objects_comb[1].animate.set_fill(RED, opacity=0.5))
        self.wait(1)
        self.play(objects_comb[1].animate.set_fill(WHITE), 
                  objects_comb[2].animate.set_fill(RED, opacity=0.5))
        self.wait(1)
        self.play(objects_comb[0].animate.set_fill(WHITE),
                  objects_comb[1].animate.set_fill(WHITE))
        self.play(objects_comb[1].animate.set_fill(RED, opacity=0.5), 
                  objects_comb[2].animate.set_fill(RED, opacity=0.5))
        self.wait(2)

        self.play(FadeOut(comb_text), FadeOut(comb_instructions), FadeOut(objects_comb))
        self.play(FadeOut(title))