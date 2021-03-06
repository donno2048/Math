# Sorry for the bad quality of the code and the video, made it in a night...
from manim import (Scene, MathTex, Create, FadeOut, LEFT,
                   RIGHT, DOWN, UP, SVGMobject, Transform,
                   Uncreate, AnimationGroup, Wiggle, Text,
                   VGroup, GRAY, WHITE, MarkupText, Paragraph,
                   ImageMobject, FadeIn, Dot, Line, Angle) # I really hate wildcard imports
from os import remove
from functools import reduce
from PIL import Image
from requests import get
class MainScene(Scene):
    def construct(self):
        text = MarkupText("I see a lot of math videos out there talking about specific areas in math but not enough about what <b>is</b> math, this video is all about that").scale(.5)
        topics = ["Numbers", "Zermelo–Fraenkel set theory", "Gödel's incompleteness theorems", "Worst case scenario"]
        Types = [Numbers, Set, Godel, NewMath]
        v = [Text(topics[i], color=GRAY).shift((i - len(topics) // 2) * DOWN) for i in range(len(topics))]
        v_2 = list(map(lambda i: i.copy().scale(1.25).set_color(WHITE), v))
        self.play(Create(text))
        self.wait(4)
        self.play(FadeOut(text))
        self.wait(1)
        for T in range(len(topics)):
            vc = list(map(lambda i: i.copy(), v))
            self.play(AnimationGroup(*[Create(i) for i in vc]))
            self.wait(2)
            self.play(Transform(vc[T], v_2[T]))
            self.play(AnimationGroup(*[FadeOut(i) for i in vc]))
            self.wait(1)
            Types[T].construct(self)
        self.wait(2)
        self.play(Create(Text("Thanks for watching")))
        self.wait(2)
class Numbers(Scene):
    def construct(self):
        types = ["natural", "whole", "rational", "real"]
        v = [Text("The %s numbers" % types[i], color=GRAY).shift((i - 2) * DOWN) for i in range(4)] + [Text("Infinity", color=GRAY).shift(2 * DOWN)]
        v_2 = list(map(lambda i: i.copy().scale(1.25).set_color(WHITE), v))
        Types = [N, Z, Q, R, Infinity]
        for T in range(5):
            vc = list(map(lambda i: i.copy(), v))
            self.play(AnimationGroup(*[Create(i) for i in vc]))
            self.wait(2)
            self.play(Transform(vc[T], v_2[T]))
            self.play(AnimationGroup(*[FadeOut(i) for i in vc]))
            self.wait(1)
            Types[T].construct(self)
class Set(Scene):
    def construct(self):
        main = Text("Zermelo–Fraenkel set theory is basically the\naxioms we use in mathematics to show everything").scale(.5)
        axioms_text = Text("The axioms are").scale(.5).shift(3 * UP)
        axioms = Paragraph("Two sets are equal if they have the same elements", "Every non-empty set contains an element which doesn't have any of the main set's elements", "Any definable group of elements from a set is a set itself", "For every pair of sets we can create a new set which contains them both", "For every set of sets we can create a new set which contains all the elements from all the sets", "Any definable function on the elements of a set will turn it into a new set", "There is a set containing the empty set which for every set in it, it contains a set of this set and its elements", "For every set we can create a new set containing every subset of it", line_spacing=2).scale(.25).shift(UP)
        formulas = VGroup(MathTex("\\forall_{a,\\,b}\\left(\\forall_cc\\in a\\Leftrightarrow c\\in b\\right)\\Rightarrow a=b").scale(.5).shift(2.5 * UP), MathTex("a\\neq\\varnothing\\Rightarrow\\exists_{b\\in a}a\\cap b=\\varnothing").scale(.5).shift(2 * UP), MathTex("\\forall_{i\\in I}\\forall_{w_i}\\forall_A\\exists_B\\forall_x\\left(x\\in B\\Leftrightarrow\\left(x\\in A\\land\\phi(x,\\,w_i,\\,A)\\right)\\right)").scale(.5).shift(1.5 * UP), MathTex("\\forall_{a,\\,b}\\exists_ca,\\,b\\in c").scale(.5).shift(UP), MathTex("\\forall_a\\exists_b\\forall_{c\\in a}\\forall_{d\\in c}d\\in b").scale(.5).shift(.5 * UP), MathTex("\\forall_a\\forall_{w_1,\\,w_2,\\,\\dots}\\left(x\\in a\\Rightarrow\\mid\\{y|\\phi\\}\\mid=1\\right)\Rightarrow\\exists_b\\forall_{x\\in a}\\exists_{y\\in b}\\phi").scale(.5), MathTex("\\exists_a\\varnothing\\in a\\land\\forall_{b\\in a}b\\cup\\{b\\}\\in a").scale(.5).shift(.5 * DOWN), MathTex("\\forall_a\\exists_b\\forall_{c\\subseteq a}c\\in b").scale(.5).shift(DOWN))
        text = Text("You might think this is not enough for actual math but in 1910 the mathematicians\nAlfred Whitehead and Bertrand Russell prove just from those rules that 1+1=2\n(Principia Mathematica page 362)").scale(.25).shift(3 * UP)
        image = ImageMobject(Image.open(get("https://i.imgur.com/EwOJXI4.jpg", stream=True).raw)).scale(.5).shift(DOWN) # I think it's better to add the image to imgur and not to have to save it locally if the whole script is a single file...
        self.play(Create(main))
        self.wait(2)
        self.play(FadeOut(main))
        self.wait(1)
        self.play(Create(axioms_text))
        self.play(Create(axioms))
        self.wait(10)
        self.play(Transform(axioms, formulas))
        self.wait(5)
        self.play(AnimationGroup(FadeOut(axioms_text), FadeOut(axioms)))
        self.wait(1)
        self.play(Create(text))
        self.play(FadeIn(image))
        self.wait(4)
        self.play(AnimationGroup(FadeOut(text), FadeOut(image)))
        self.wait(1)
class Godel(Scene):
    def construct(self):
        texts = [Text("Kurt Gödel was an Austrian mathematician he's considered\nto be one of the greatest logicians of all times").scale(.5), Text("In 1931 he managed to show every axiomatic\nsystem is either not consistent or not complete").scale(.5).shift(3 * UP), Text("Not consistent - some statements are both true and false").scale(.25).shift(2 * UP), Text("Not complete - there are statements we cannot know whether they are true or false").scale(.25).shift(1.5 * UP), Text("He went furthermore and proved you cannot show that an\naxiomatic system is consistent if it's consistent from its own rules").scale(.5), Text("This means our set of axioms the\nZermelo–Fraenkel set theory is maybe not consistent").scale(.5), Text("We already know it's not complete, here is a problem we will never be able to answer").scale(.45).shift(3 * UP), Text("Given two matrices").scale(.25).shift(2 * UP), Text("We cannot know for every pair if we can concatenate them into a nilpotent matrix\n(even for size 15x15 alone)").scale(.25).shift(UP)]
        maths = [MathTex("A").scale(.5).shift(LEFT), MathTex("B").scale(.5).shift(RIGHT), VGroup(Text("Can"), MathTex("A^{a_1}\\cdot B^{b_1}\\cdot A^{a_2}\\cdot B^{b_2}\\cdot\\dots"), Text("be nilpotent?")).arrange(RIGHT, buff=1).scale(.5).shift(DOWN)]
        self.play(Create(texts[0]))
        self.wait(5)
        self.play(FadeOut(texts[0]))
        self.wait(1)
        for text in texts[1: 4]: self.play(Create(text))
        self.wait(8)
        self.play(AnimationGroup(*[FadeOut(text) for text in texts[1: 4]]))
        self.wait(2)
        Proof.construct(self)
        self.play(Create(texts[4]))
        self.wait(4)
        self.play(FadeOut(texts[4]))
        self.wait(1)
        self.play(Create(texts[5]))
        self.wait(3)
        self.play(FadeOut(texts[5]))
        self.wait(1)
        self.play(Create(texts[6]))
        self.wait(2)
        self.play(Create(texts[7]))
        self.wait(1)
        self.play(AnimationGroup(Create(maths[0]), Create(maths[1])))
        self.wait(1)
        self.play(AnimationGroup(Create(texts[8]), Create(maths[2])))
        self.wait(5)
        self.play(AnimationGroup(*[FadeOut(math) for math in maths], *[FadeOut(text) for text in texts[6:]]))
        self.wait(1)
class NewMath(Scene):
    def construct(self):
        texts = ["What about the worst case scenario where we find our axioms to be inconsistent?", "Well, we will invent a new math", "It's not the first time we have done it", "The ZFC set of axioms itself was introduced because of Russell's paradox", "And there are even weirder cases like the Lobachevskian geometry"]
        texts = list(map(lambda i: Text(i).scale(.5), texts))
        for i in range(4):
            self.play(Create(texts[i]))
            self.wait(2)
            self.play(FadeOut(texts[i]))
            self.wait(1)
        Russell.construct(self)
        self.play(Create(texts[4]))
        self.wait(2)
        self.play(FadeOut(texts[4]))
        self.wait(1)
        Lobachevskian.construct(self)
class N(Scene):
    def construct(self):
        N = MathTex("\\mathbb N")
        texts = ["First, we have the \"natural numbers\"", "Those are probably the most frequently used numbers", "We define them as all possible amounts of elements in a (finite) group", "Let me explain", "We define three as a group with three elements", "Like a house", "With two parents and a kid", "Three and a half is not a natural number since\nwe cannot have three and a half elements", "Even if we have only half of a baby", "This half is still one element"]
        texts = list(map(lambda i: Text(i).shift(2 * UP).scale(.5), texts))
        numbers = MathTex(",\\,".join(list(map(str, range(10)))) + "\\,." * 3)
        three = MathTex("3=\\{\\text{first},\\,\\text{second},\\,\\text{third}\\}")
        open('house.svg', "w").write('<svg xmlns="http://www.w3.org/2000/svg" width="463.89285" height="438.87704"><g><g><path fill="#ffffff" stroke-width="0.4" stroke-miterlimit="4" id="rect2391" d="m394.805786,223.09549l0,0zm0,0l-162.8125,-144.1875l-162.90625,144.25l0,206.125c0,5.323364 4.30162,9.59375 9.625,9.59375l101.812515,0l0,-90.375c0,-5.323425 4.27037,-9.625 9.59375,-9.625l83.656235,0c5.323364,0 9.59375,4.301636 9.59375,9.625l0,90.375l101.84375,0c5.323364,0 9.593781,-4.270325 9.59375,-9.59375l0,-206.1875zm-325.71875,0.0625l0,0z"/><path fill="#ffffff" stroke-width="0.4" stroke-miterlimit="4" id="path2399" d="m231.048492,-0.000305l-231.0485,204.583557l24.338306,27.457397l207.655384,-183.884186l207.608124,183.884186l24.291046,-27.457397l-231.001251,-204.583557l-0.897919,1.039703l-0.94519,-1.039703z"/><path fill="#ffffff" stroke-width="0.4" stroke-miterlimit="4" id="rect2404" d="m69.087036,29.44873l58.571442,0l-0.510376,34.691101l-58.061066,52.451752l0,-87.142853z"/></g></g></svg>')
        open('man.svg', "w").write('<svg xmlns="http://www.w3.org/2000/svg"><g><g><circle fill="#ffffff" cx="26.677" cy="4.383" r="4.383"/><path fill="#ffffff" d="M40.201,28.096c-1.236-13.887-7.854-16.657-7.854-16.657s-6.396-3.845-13.129,1.052    c-4.365,3.973-5.373,10.038-6.063,15.896c-0.349,2.977,4.307,2.941,4.653,0c0.412-3.496,1-7.008,2.735-9.999l-0.008,3.375    l-0.032,16.219v12.867c0,1.383,1.014,2.506,2.438,2.506c1.423,0,2.578-1.123,2.578-2.506V32.457h2.278c0,4.309,0,14.144,0,18.451    c0,3,4.652,3,4.652,0c0-4.309,0-8.619,0-12.927l0.197-16.251c0.002-1.551,0.004-2.937,0.004-3.901    c1.859,3.046,2.473,6.664,2.896,10.265C35.895,31.037,40.55,31.073,40.201,28.096z"/></g></g></svg>')
        open('halfman.svg', "w").write('<svg xmlns="http://www.w3.org/2000/svg"><g><g><g><circle fill="#ffffff" r="4.33643" cy="4.35971" cx="20.10884"/><path fill="#ffffff" d="m33.48915,28.07271c-1.22287,-13.887 -7.77055,-16.657 -7.77055,-16.657s-6.32804,-3.845 -12.9895,1.052c-4.31862,3.973 -5.31591,10.038 -5.99858,15.896c-0.34529,2.977 4.26124,2.941 4.60356,0c0.40762,-3.496 0.98937,-7.008 2.70594,-9.999l-0.00791,3.375l-0.03166,16.219l0,12.867c0,1.383 1.00323,2.506 2.4121,2.506c1.40788,0 2.55061,-1.123 2.55061,-2.506l0,-18.392l2.2538,0c0,4.309 0,14.144 0,18.451c0,3 4.60257,3 4.60257,0c0,-4.309 0,-8.619 0,-12.927l0.19491,-16.251c0.00198,-1.551 0.00396,-2.937 0.00396,-3.901c1.83925,3.046 2.44672,6.664 2.86523,10.265c0.34529,2.943 4.95083,2.979 4.60554,0.002z"/></g></g><rect fill="#000000" height="53.34188" width="20.28775" y="0" x="20"/></g></svg>')
        house = SVGMobject('house.svg')
        man1 = SVGMobject('man.svg').shift(2 * LEFT)
        halfkid = SVGMobject('halfman.svg', height=1).shift(2 * DOWN)
        man2 = man1.copy().shift(4 * RIGHT)
        kid = man1.copy().shift(2 * RIGHT).shift(2 * DOWN).scale(.5)
        remove('house.svg')
        remove('man.svg')
        remove('halfman.svg')
        self.play(AnimationGroup(Create(N), Create(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(N), FadeOut(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(Create(numbers), Create(texts[1])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(numbers), FadeOut(texts[1])))
        self.wait(2)
        self.play(AnimationGroup(Create(three), Create(texts[2])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(three), FadeOut(texts[2])))
        self.wait(2)
        self.play(Create(texts[3]))
        self.play(Create(house))
        self.play(FadeOut(texts[3]))
        self.play(Create(texts[4]))
        self.play(Create(man1))
        self.play(FadeOut(texts[4]))
        self.play(Create(texts[5]))
        self.play(Create(man2))
        self.play(FadeOut(texts[5]))
        self.play(Create(texts[6]))
        self.play(Create(kid))
        self.play(FadeOut(texts[6]))
        self.play(Create(texts[7]))
        self.wait(4)
        self.play(FadeOut(texts[7]))
        self.play(Create(texts[8]))
        self.play(Transform(kid, halfkid))
        self.wait(2)
        self.play(FadeOut(texts[8]))
        self.play(Create(texts[9]))
        self.wait(2)
        self.play(Wiggle(kid))
        self.play(AnimationGroup(Uncreate(kid), Uncreate(man1), Uncreate(man2), Uncreate(house)))
        self.play(FadeOut(texts[9]))
        self.wait(2)
class Z(Scene):
    def construct(self):
        Z = MathTex("\\mathbb Z")
        texts = ["Then we have the \"whole numbers\"", "Those are the positive and negative numbers", "But in order to use them mathematically we can't just\n\"invent\" negative numbers, we need to well define them too", "First we define addition on the natural numbers", "Remember we said every natural number is a size of a group?", "Take this group", "Which has A elements", "And this group", "Which has B elements", "Such that those groups has no shared element", "Then we define the disjoint union as the group\nwith all the elements from both groups", "And finally we define the sum of A and B as\nthe amount of elements in the disjoint union", "Now we'll define a new operator called minus", "Now we need two groups", "With sizes", "Such that", "We know there must exist one since we can take the original groups, so\nwe define A - B to be the group of all possible groups with this property", "If you take every two natural number and minus them,\nthe resulting group is what we call the whole numbers"]
        texts = list(map(lambda i: Text(i).shift(2 * UP).scale(.5), texts))
        numbers = MathTex(".\\," * 3 + ",\\,".join(list(map(str, range(-5, 6)))) + "\\,." * 3)
        minus_one = MathTex("-1=\\{c,\\,d\\in\\mathbb N\\mid 0+c=1+d\\}")
        plus = MathTex("+")
        minus = MathTex("-")
        groups = [MathTex("a").shift(LEFT), MathTex("\\mid a\\mid=A").shift(2 * LEFT + DOWN), MathTex("b").shift(RIGHT), MathTex("\\mid b\\mid=B").shift(2 * RIGHT + DOWN), MathTex("a\\cap b=\\varnothing").shift(2 * DOWN), MathTex("c=a\\cup b").shift(UP), MathTex("A+B=\\mid c\\mid")]
        groups_2 = list(map(lambda i: i.copy(), groups[:4])) + [MathTex("c").shift(6 * LEFT), MathTex("d").shift(6 * RIGHT), MathTex("\\mid c\\mid=C").shift(6 * LEFT + DOWN), MathTex("\\mid d\\mid=D").shift(6 * RIGHT + DOWN), MathTex("A+C=B+D").shift(2 * DOWN), MathTex("A-B=\\{c,\\,d\\in\\mathbb N\\mid A+\\mid c\\mid=\\mid d\\mid+B\\}")]
        self.play(AnimationGroup(Create(Z), Create(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(Z), FadeOut(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(Create(numbers), Create(texts[1])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(numbers), FadeOut(texts[1])))
        self.wait(2)
        self.play(Create(texts[2]))
        self.wait(7)
        self.play(FadeOut(texts[2]))
        self.wait(2)
        self.play(Create(texts[3]))
        self.play(Create(plus))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[3]), FadeOut(plus)))
        self.wait(2)
        self.play(Create(texts[4]))
        self.wait(2)
        self.play(FadeOut(texts[4]))
        self.wait(2)
        self.play(Create(texts[5]))
        self.play(Create(groups[0]))
        self.wait(2)
        self.play(FadeOut(texts[5]))
        self.wait(1)
        self.play(Create(texts[6]))
        self.play(Create(groups[1]))
        self.wait(2)
        self.play(FadeOut(texts[6]))
        self.wait(1)
        self.play(Create(texts[7]))
        self.play(Create(groups[2]))
        self.wait(2)
        self.play(FadeOut(texts[7]))
        self.wait(1)
        self.play(Create(texts[8]))
        self.play(Create(groups[3]))
        self.wait(2)
        self.play(FadeOut(texts[8]))
        self.wait(1)
        self.play(Create(texts[9]))
        self.play(Create(groups[4]))
        self.wait(2)
        self.play(FadeOut(texts[9]))
        self.wait(1)
        self.play(Create(texts[10]))
        self.play(Create(groups[5]))
        self.wait(4)
        self.play(FadeOut(texts[10]))
        self.wait(1)
        self.play(Create(texts[11]))
        self.play(AnimationGroup(*[Uncreate(equation) for equation in groups[:-1]]))
        self.play(Create(groups[6]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[11]), Uncreate(groups[6])))
        self.wait(1)
        self.play(Create(texts[12]))
        self.play(Create(minus))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[12]), FadeOut(minus)))
        self.wait(2)
        self.play(Create(texts[5]))
        self.play(Create(groups_2[0]))
        self.wait(2)
        self.play(FadeOut(texts[5]))
        self.wait(1)
        self.play(Create(texts[6]))
        self.play(Create(groups_2[1]))
        self.wait(2)
        self.play(FadeOut(texts[6]))
        self.wait(1)
        self.play(Create(texts[7]))
        self.play(Create(groups_2[2]))
        self.wait(2)
        self.play(FadeOut(texts[7]))
        self.wait(1)
        self.play(Create(texts[8]))
        self.play(Create(groups_2[3]))
        self.wait(2)
        self.play(FadeOut(texts[8]))
        self.wait(1)
        self.play(Create(texts[13]))
        self.play(AnimationGroup(Create(groups_2[4]), Create(groups_2[5])))
        self.wait(2)
        self.play(FadeOut(texts[13]))
        self.wait(1)
        self.play(Create(texts[14]))
        self.play(AnimationGroup(Create(groups_2[6]), Create(groups_2[7])))
        self.wait(2)
        self.play(FadeOut(texts[14]))
        self.wait(1)
        self.play(Create(texts[15]))
        self.play(Create(groups_2[8]))
        self.wait(2)
        self.play(FadeOut(texts[15]))
        self.play(AnimationGroup(*[Uncreate(equation) for equation in groups_2[:-1]]))
        self.wait(1)
        self.play(Create(texts[16]))
        self.play(Create(groups_2[9]))
        self.wait(5)
        self.play(AnimationGroup(FadeOut(texts[16]), Uncreate(groups_2[9])))
        self.wait(1)
        self.play(Create(texts[17]))
        self.wait(5)
        self.play(FadeOut(texts[17]))
        self.wait(1)
class Q(Scene):
    def construct(self):
        Q = MathTex("\\mathbb Q")
        texts = ["Now we can view the \"rational numbers\"", "They're known by this story about Pythagoras who thought all the\nnumbers can be represented by a fraction between two whole numbers", "Defining the rationals from the wholes is very\nsimilar to defining the wholes from the naturals", "First, we define a new operation on pairs of\nnatural numbers and whole numbers, called the product", "Take this group", "Which has A elements", "Where each element is B, a whole number", "Then apply the + operator on the first and second elements", "Then do the same with the result and the third element and continue recursively", "Take the result and this is what we define as the product of A and B", "Now we can define the division operator", "Take a pair of a whole number and a natural number", "Now we need a pair of a whole number and a natural number", "Such that", "We know there must exist one since we can take the original groups, so\nwe define A / B to be the group of all possible groups with this property", "If you take every pair of whole number and natural number and divide\nthem, the resulting group is what we call the rational numbers"]
        texts = list(map(lambda i: Text(i).shift(2 * UP).scale(.5), texts))
        numbers = MathTex(".\\," * 3 + ",\\,".join(list(map(lambda i: "\\frac{%d}%d" % i, list(zip(list(range(-1, 2)) + list(range(-2, 3)) + list(range(-3, 4)), reduce(lambda a, b: a + b,[[i] * (2 * i + 1) for i in range(1, 4)])))))) + "\\,." * 3)
        product = MathTex("\\cdot")
        division = MathTex("/")
        B = MathTex("B,\\,").shift(2 * DOWN + 3 * LEFT)
        B_ = MathTex("B").shift(3 * DOWN + 3 * LEFT)
        plus = MathTex("+").shift(3 * DOWN + 2 * LEFT)
        groups = [MathTex("a"), MathTex("\\mid a\\mid=A").shift(DOWN), MathTex("a=\\{").shift(2 * DOWN + 6 * LEFT), B, B.copy().shift(2 * RIGHT), B.copy().shift(4 * RIGHT), MathTex("\\dots").shift(2 * DOWN, 3 * RIGHT), MathTex("\\}").shift(2 * DOWN, 6 * RIGHT), plus, plus.copy().shift(2 * RIGHT), plus.copy().shift(4 * RIGHT), MathTex("A\\cdot B=").shift(3 * DOWN + 5 * LEFT)]
        groups_2 = [MathTex("A").shift(2 * LEFT), MathTex("B").shift(2 * RIGHT), MathTex("C").shift(LEFT), MathTex("D").shift(RIGHT), MathTex("\\cdot").shift(1.5 * LEFT), MathTex("="), MathTex("\\cdot").shift(1.5 * RIGHT)]
        self.play(AnimationGroup(Create(Q), Create(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(Q), FadeOut(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(Create(numbers), Create(texts[1])))
        self.wait(7)
        self.play(AnimationGroup(FadeOut(numbers), FadeOut(texts[1])))
        self.wait(2)
        self.play(Create(texts[2]))
        self.wait(2)
        self.play(FadeOut(texts[2]))
        self.wait(2)
        self.play(Create(texts[3]))
        self.play(Create(product))
        self.wait(4)
        self.play(AnimationGroup(FadeOut(texts[3]), FadeOut(product)))
        self.wait(1)
        self.play(Create(texts[4]))
        self.play(Create(groups[0]))
        self.wait(2)
        self.play(FadeOut(texts[4]))
        self.wait(1)
        self.play(Create(texts[5]))
        self.play(Create(groups[1]))
        self.wait(2)
        self.play(FadeOut(texts[5]))
        self.wait(1)
        self.play(Create(texts[6]))
        self.play(AnimationGroup(*[Create(i) for i in groups[2: 8]]))
        self.wait(2)
        self.play(FadeOut(texts[6]))
        self.wait(1)
        self.play(Create(texts[7]))
        self.play(AnimationGroup(Transform(groups[3], B_), Transform(groups[4], B_.copy().shift(2 * RIGHT)), Create(groups[8])))
        self.wait(2)
        self.play(FadeOut(texts[7]))
        self.wait(1)
        self.play(Create(texts[8]))
        self.play(AnimationGroup(Transform(groups[5], B_.copy().shift(4 * RIGHT)), Create(groups[9]), Transform(groups[6], groups[6].shift(DOWN)), Create(groups[10])))
        self.wait(2)
        self.play(FadeOut(texts[8]))
        self.wait(1)
        self.play(Create(texts[9]))
        self.play(Create(groups[11]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[9]), *[FadeOut(i) for i in groups]))
        self.wait(1)
        self.play(Create(texts[10]))
        self.play(Create(division))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[10]), FadeOut(division)))
        self.wait(1)
        self.play(Create(texts[11]))
        self.play(AnimationGroup(Create(groups_2[0]), Create(groups_2[1])))
        self.wait(2)
        self.play(FadeOut(texts[11]))
        self.wait(1)
        self.play(Create(texts[12]))
        self.play(AnimationGroup(Create(groups_2[2]), Create(groups_2[3])))
        self.wait(2)
        self.play(FadeOut(texts[12]))
        self.wait(1)
        self.play(Create(texts[13]))
        self.play(AnimationGroup(*[Create(i) for i in groups_2[4: 7]]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[13]), *[FadeOut(i) for i in groups_2]))
        self.wait(1)
        self.play(Create(texts[14]))
        self.wait(5)
        self.play(FadeOut(texts[14]))
        self.wait(1)
        self.play(Create(texts[15]))
        self.wait(5)
        self.play(FadeOut(texts[15]))
        self.wait(1)
class R(Scene):
    def construct(self):
        R = MathTex("\\mathbb R")
        texts = ["The \"real numbers\" are a bit more complex", "First, we define series as a group with an order", "Now we can define zero convergencies", "We'll say a series converges to 0 if for any value e bigger\nthan 0 we can find an index n in the series where for every\nN bigger than it the N-th element is smaller in size than e", "Now we define a differences series of a series A as the series of the first\nelement in A minus the second one, then the second minus the third and so on", "And then we define a Cauchy series as a\nseries whose differences series converges to 0", "If we have a series A and a number B we'll define A - B", "Now we say a number B is real if there is a Cauchy series\nA on the rational numbers such that A – B converges to 0", "We know not every real number is rational since\nfor example the series: 3, 3.1, 3.14, 3.141, …\nIs a Cauchy series (because the difference is smaller\nthan 10^-n which converges to 0) But pi isn't rational"]
        texts = list(map(lambda i: Text(i).shift(2 * UP).scale(.5), texts))
        groups = [MathTex("(\\overrightarrow{a,\\,b,\\,c,\\,\\dots})"), MathTex("\\to0"), MathTex("N>n\\Rightarrow\\mid a_N\\mid<e"), MathTex("A=\\{a_1,\\,a_2,\\,a_3,\\,\\dots\\}").scale(.5).shift(UP), MathTex("D=\\{a_1-a_2,\\,a_2-a_3,\\,a_3-a_4,\\,\\dots\\}").scale(.5).shift(DOWN), MathTex("A=\\{a_1,\\,a_2,\\,a_3,\\,\\dots\\}\\\\A-B=\\{a_1-B,\\,a_2-B,\\,a_3-B,\\,\\dots\\}").scale(.5)]
        self.play(AnimationGroup(Create(R), Create(texts[0])))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(R), FadeOut(texts[0])))
        self.wait(2)
        self.play(Create(texts[1]))
        self.play(Create(groups[0]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[1]), FadeOut(groups[0])))
        self.wait(1)
        self.play(Create(texts[2]))
        self.play(Create(groups[1]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[2]), FadeOut(groups[1])))
        self.wait(1)
        self.play(Create(texts[3]))
        self.play(Create(groups[2]))
        self.wait(6)
        self.play(AnimationGroup(FadeOut(texts[3]), FadeOut(groups[2])))
        self.wait(1)
        self.play(Create(texts[4]))
        self.play(Create(groups[3]))
        self.wait(1)
        self.play(Create(groups[4]))
        self.wait(4)
        self.play(AnimationGroup(FadeOut(texts[4]), FadeOut(groups[3]), FadeOut(groups[4])))
        self.wait(1)
        self.play(Create(texts[5]))
        self.wait(4)
        self.play(FadeOut(texts[5]))
        self.wait(1)
        self.play(Create(texts[6]))
        self.play(Create(groups[5]))
        self.wait(4)
        self.play(AnimationGroup(FadeOut(texts[6]), FadeOut(groups[5])))
        self.wait(1)
        self.play(Create(texts[7]))
        self.wait(4)
        self.play(FadeOut(texts[7]))
        self.wait(1)
        self.play(Create(texts[8]))
        self.wait(8)
        self.play(FadeOut(texts[8]))
        self.wait(1)
class Infinity(Scene):
    def construct(self):
        Infinity = MathTex("\\infty")
        texts = [MarkupText("Now you must think <span fgcolor=\"yellow\">\"what about infinity? he's a number too, those definitions completely ignore him\"</span>").scale(.5).shift(2 * UP), Text("Well you're wrong infinity isn’t a number if\nyou try to use it as one you get horrible results").scale(.5), Text("For example let's take this value").scale(.5).shift(3 * UP)]
        down = MathTex("\\Downarrow").scale(.5).shift(UP)
        equalities = [MathTex("A=2+4+8+16+\\dots").scale(.5).shift(1.5 * UP), down, MathTex("A=2\\left(1+2+4+8+16+\\dots\\right)").scale(.5).shift(.5 * UP), down.copy().shift(DOWN), MathTex("A=2+2\\left(2+4+8+16+\\dots\\right)").scale(.5).shift(.5 * DOWN), down.copy().shift(2 * DOWN), MathTex("A=2+2A").scale(.5).shift(1.5 * DOWN), down.copy().shift(3 * DOWN), MathTex("\\infty=2+2\\infty\\Rightarrow-\\infty=2").scale(.5).shift(2.5 * DOWN), MathTex("A=\\sum_{n=1}^\\infty2^n=2\\sum_{n=1}^\\infty2^{n-1}=2\\sum_{n=0}^\\infty2^n=2+2\\sum_{n=1}^\\infty2^n=2+2A").scale(.25).shift(5 * LEFT)]
        self.play(AnimationGroup(Create(texts[0]), Create(Infinity)))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[0]), FadeOut(Infinity)))
        self.wait(1)
        self.play(Create(texts[1]))
        self.wait(4)
        self.play(FadeOut(texts[1]))
        self.wait(1)
        self.play(Create(texts[2]))
        for i in equalities: self.play(Create(i))
        self.wait(10)
        self.play(AnimationGroup(FadeOut(texts[2]), *[FadeOut(i) for i in equalities]))
        self.wait(1)
class Russell(Scene):
    def construct(self):
        text = Paragraph("Russell's paradox goes like this", "Let's say you have a set S containing the sets that don't contain themself", "Does S contain itself?", "If it does then it's a set that does not contain itself", "So S cannot contain itself", "But if S doesn't contain itself it's not a set that doesn't contain itself", "Therefore S contains itself", "ZFC replaced the former set of axioms to make sure a set cannot be defined like S", line_spacing=2).scale(.5)
        self.play(Create(text))
        self.wait(20)
        self.play(FadeOut(text))
        self.wait(1)
class Lobachevskian(Scene):
    def construct(self):
        texts = [Text("The Lobachevskian geometry replaced Euclid's fifth postulate in the standart geometry").scale(.45), Text("Euclid's fifth postulate").scale(.5).shift(3 * UP), Text("If there's a line and two other lines going through it such that the angles\nformed are summed to less than π in one side\nthen the intersaction is in that side").scale(.25).shift(2 * UP), Text("Was replaced with").scale(.5).shift(UP), Text("For every line and point the point is either on the line or there are more than one line through this point that doesn't intersect the line").scale(.25)]
        points = [Dot(point=[1, -2, 0]), Dot(point=[1, 0, 0]), Dot(point=[4, -3, 0]), Dot(point=[3, 2, 0]), Dot(point=[-.5, -1.5, 0])]
        lines = [Line(points[0], points[1]), Line(points[2], points[4]), Line(points[3], points[4])]
        angles = [Angle(lines[0], lines[1]), Angle(lines[2], lines[0], radius=.5), MathTex("\\alpha").scale(.45).shift([.85, -1.8, 0]), MathTex("\\beta").scale(.45).shift([.85, -.35, 0]), MathTex("\\alpha+\\beta<\\pi").scale(.5).shift(.25, -1.1, 0)]
        angles = angles[2:] # :( have to do it, second angle always breaks
        self.play(Create(texts[0]))
        self.wait(2)
        self.play(FadeOut(texts[0]))
        self.wait(1)
        self.play(Create(texts[1]))
        self.wait(1)
        self.play(Create(texts[2]))
        self.wait(5)
        self.play(AnimationGroup(*[Create(obj) for obj in points + lines + angles]))
        self.wait(5)
        self.play(AnimationGroup(*[FadeOut(obj) for obj in points + lines + angles]))
        self.wait(1)
        self.play(Create(texts[3]))
        self.wait(1)
        self.play(Create(texts[4]))
        self.wait(5)
        self.play(AnimationGroup(*[FadeOut(text) for text in texts[1:]]))
        self.wait(1)
class Proof(Scene):
    def construct(self):
        texts = [Text("This is how Gödel proved it").scale(.5), Text("Remember all these symbols we used to show the axioms?\n(If not rewind the video 50 seconds back to 8:00)").scale(.5), Text("Those are logic symbols").scale(.5), Text("Gödel toke each logic symbol and gave it a Gödel number").scale(.5).shift(3 * UP), Text("To represent every number too").scale(.5).shift(3 * UP), Text("He gave the number 0 the Gödel 1 and to s\n(in ZFC meaning plus one) the Gödel number 2").scale(.5).shift(2.5 * UP), Text("In that way you can express every natural number with only s and 0").scale(.5).shift(1.5 * UP), Text("Then he created a process to give every logic statement a Gödel number").scale(.5).shift(3 * UP), Text("For example").scale(.5).shift(3 * UP), Text("(From the Fundamental theorem of arithmetic we can know that\nfor each one of these there is one unique Gödel number)").scale(.5).shift(3 * UP), Text("The proof of a statement is made up of logic\nsymbols and therefore has its own Gödel number").scale(.5).shift(3 * UP), Text("We will now define variables").scale(.5).shift(3 * UP), Text("And a new logic operation sub(a, b, c) which means take\nthe formula which Gödel number a and replace the symbol\nwith Gödel number c with the symbol with Gödel number b").scale(.5).shift(2 * UP), Text("And lastly a new logic operator D(a, b) which means the statement\nwith Gödel number a is a proof for the statement with Gödel number b").scale(.5).shift(3 * UP), Text("The smart part of the proof is to take the Gödel number (G) of\nthe statement \"There is no proof to Gödel number sub(y, y, 11)\"").scale(.5).shift(3 * UP), Text("Now we take a new formula with a new Gödel number that says\n\"There is no proof to Gödel number sub(G, G, 11)\" what its Gödel number?").scale(.5).shift(3 * UP), Text("By definition, sub(G, G, 11) is the Gödel number of the formula that results\nfrom taking the formula with Gödel number G and substituting G anywhere there’s\na symbol with Gödel number 11. And our new formula is exactly that. Therefore\nits Gödel number is G. But it says that there is no proof for Gödel number G").scale(.5).shift(3 * UP), Text("Now it's either a paradox or we can never know").scale(.5).shift(3 * UP), Text("And that's Gödel's proof")]
        maths = [MathTex("""\\begin{tabular}{|l|l|l|}\n\\hline\nLogic sign & Gödel number & Meaning \\\\\n$0$ & 1 & zero \\\\\n$s$ & 2 & plus one \\\\\n$+$ & 3 & plus \\\\\n$=$ & 4 & equals \\\\\n$\\neg$ & 5 & not \\\\\n$\\exists$ & 6 & exists \\\\\n$($ & 7 & open bracket \\\\\n$)$ & 8 & close bracket \\\\\n$,$ & 9 & more values \\\\\n\\hline\n\\end{tabular}""").scale(.5).shift(DOWN), MathTex("2=ss0").scale(.5).shift(UP), MathTex("1+1=2").scale(.5).shift(2.5 * UP), MathTex("s0+s0=ss0").scale(.5).shift(2 * UP), MathTex("213214221").scale(.5).shift(1.5 * UP), VGroup(Text("The Gödel number of").scale(.5), MathTex("1+1=2"), Text("is").scale(.5), MathTex("2^23^15^37^211^113^417^219^223^1=55409765750839500")).arrange(RIGHT).scale(.5).shift(UP), MathTex("""\\begin{tabular}{|l|l|l|}\n\\hline\nLogic sign & Gödel number & Meaning \\\\\n$0$ & 1 & zero \\\\\n$s$ & 2 & plus one \\\\\n$+$ & 3 & plus \\\\\n$=$ & 4 & equals \\\\\n$\\neg$ & 5 & not \\\\\n$\\exists$ & 6 & exists \\\\\n$($ & 7 & open bracket \\\\\n$)$ & 8 & close bracket \\\\\n$,$ & 9 & more values \\\\\n$x$ & 10 & variable \\\\\n$y$ & 11 & variable \\\\\n\\hline\n\\end{tabular}""").scale(.5).shift(DOWN), MathTex("""\\begin{tabular}{|l|l|l|}\n\\hline\nLogic sign & Gödel number & Meaning \\\\\n$0$ & 1 & zero \\\\\n$s$ & 2 & plus one \\\\\n$+$ & 3 & plus \\\\\n$=$ & 4 & equals \\\\\n$\\neg$ & 5 & not \\\\\n$\\exists$ & 6 & exists \\\\\n$($ & 7 & open bracket \\\\\n$)$ & 8 & close bracket \\\\\n$,$ & 9 & more values \\\\\n$x$ & 10 & variable \\\\\n$y$ & 11 & variable \\\\\nsub & 12 & substitute \\\\\n\\hline\n\\end{tabular}""").scale(.5).shift(DOWN), MathTex("""\\begin{tabular}{|l|l|l|}\n\\hline\nLogic sign & Gödel number & Meaning \\\\\n$0$ & 1 & zero \\\\\n$s$ & 2 & plus one \\\\\n$+$ & 3 & plus \\\\\n$=$ & 4 & equals \\\\\n$\\neg$ & 5 & not \\\\\n$\\exists$ & 6 & exists \\\\\n$($ & 7 & open bracket \\\\\n$)$ & 8 & close bracket \\\\\n$,$ & 9 & more values \\\\\n$x$ & 10 & variable \\\\\n$y$ & 11 & variable \\\\\nsub & 12 & substitute \\\\\nD & 13 & proof \\\\\n\\hline\n\\end{tabular}""").scale(.5).shift(DOWN), MathTex("G=\\neg\\exists x(D(x,\\,sub(y,\\,y,\\,11)))").scale(.5).shift(2 * UP), VGroup(Text("The Gödel number of").scale(.5), MathTex("\\neg\\exists x(D(x,\\,sub(G,\\,G,\\,11)))"), Text("is").scale(.5), MathTex("?")).arrange(RIGHT).scale(.5).shift(1.5 * UP)]
        for text in texts[:3]:
            self.play(Create(text))
            self.wait(3)
            self.play(FadeOut(text))
            self.wait(1)
        self.play(Create(texts[3]))
        self.wait(2)
        self.play(Create(maths[0]))
        self.wait(5)
        self.play(FadeOut(texts[3]))
        self.wait(1)
        for text in texts[4: 7]:
            self.play(Create(text))
        self.play(Create(maths[1]))
        self.wait(10)
        self.play(AnimationGroup(FadeOut(maths[1]), *[FadeOut(text) for text in texts[4: 7]]))
        self.wait(1)
        self.play(Create(texts[7]))
        self.wait(2)
        self.play(FadeOut(texts[7]))
        self.wait(1)
        self.play(Create(texts[8]))
        for math in maths[2: 6]:
            self.play(Create(math))
            self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[8]), *[FadeOut(math) for math in maths[2: 6]]))
        self.wait(1)
        self.play(Create(texts[9]))
        self.wait(5)
        self.play(FadeOut(texts[9]))
        self.wait(1)
        self.play(Create(texts[10]))
        self.wait(5)
        self.play(FadeOut(texts[10]))
        self.wait(1)
        self.play(Create(texts[11]))
        self.wait(2)
        self.play(Transform(maths[0], maths[6]))
        self.wait(2)
        self.play(FadeOut(texts[11]))
        self.wait(1)
        self.play(Create(texts[12]))
        self.wait(5)
        self.play(Transform(maths[0], maths[7]))
        self.wait(2)
        self.play(FadeOut(texts[12]))
        self.wait(1)
        self.play(Create(texts[13]))
        self.wait(4)
        self.play(Transform(maths[0], maths[8]))
        self.wait(2)
        self.play(FadeOut(texts[13]))
        self.wait(1)
        self.play(Create(texts[14]))
        self.wait(2)
        self.play(Create(maths[9]))
        self.wait(2)
        self.play(FadeOut(texts[14]))
        self.wait(1)
        self.play(Create(texts[15]))
        self.wait(2)
        self.play(Create(maths[10]))
        self.wait(2)
        self.play(FadeOut(texts[15]))
        self.wait(1)
        self.play(Create(texts[16]))
        self.wait(15)
        self.play(FadeOut(texts[16]))
        self.wait(1)
        self.play(Create(texts[17]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(texts[17]), FadeOut(maths[0]), FadeOut(maths[9]), FadeOut(maths[10])))
        self.wait(1)
        self.play(Create(texts[18]))
        self.wait(2)
        self.play(FadeOut(texts[18]))
        self.wait(1)