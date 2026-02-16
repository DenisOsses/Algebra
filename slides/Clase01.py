from manim import *

class Clase01(Scene):
    def construct(self):
        title = Text("Clase 1", font_size=48)
        subtitle = Text("Proposiciones y conectivos lógicos", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Proposiciones y conectivos lógicos":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
