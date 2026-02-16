from manim import *

class Clase21(Scene):
    def construct(self):
        title = Text("Clase 21", font_size=48)
        subtitle = Text("Perpendicularidad de rectas. Vector proyección", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Perpendicularidad de rectas. Vector proyección":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
