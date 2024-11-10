from manim import *

class PermutationCombination(Scene):
    def construct(self):
        title = Text("Permutation and Combination", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Permutations
        perm_text = Text("Permutations (nPr)", font_size=36).shift(UP * 2)
        self.play(Write(perm_text))
        self.wait(1)

        perm_formula = MathTex("nPr = \\frac{n!}{(n-r)!}").next_to(perm_text, DOWN)
        self.play(Write(perm_formula))
        self.wait(2)

        n_val = MathTex("n = 5").next_to(perm_formula, DOWN).shift(LEFT)
        r_val = MathTex("r = 3").next_to(n_val, RIGHT).shift(UP)
        
        self.play(Write(n_val), Write(r_val))
        self.wait(1)

        perm_result = MathTex("5P3 = \\frac{5!}{(5-3)!} = \\frac{5!}{2!} = 60").next_to(r_val, DOWN)
        self.play(Write(perm_result))
        self.wait(2)

        self.play(FadeOut(perm_text), FadeOut(perm_formula), FadeOut(n_val), FadeOut(r_val), FadeOut(perm_result))

        # Combinations
        comb_text = Text("Combinations (nCr)", font_size=36).shift(UP * 2)
        self.play(Write(comb_text))
        self.wait(1)

        comb_formula = MathTex("nCr = \\frac{n!}{r!(n-r)!}").next_to(comb_text, DOWN)
        self.play(Write(comb_formula))
        self.wait(2)

        self.play(Write(n_val), Write(r_val))
        self.wait(1)

        comb_result = MathTex("5C3 = \\frac{5!}{3!2!} = 10").next_to(r_val, DOWN)
        self.play(Write(comb_result))
        self.wait(2)

        self.play(FadeOut(comb_text), FadeOut(comb_formula), FadeOut(comb_result))

        self.play(FadeOut(title))