from manim import *

class Clase23(Scene):
    def construct(self):
        title = Text("Clase 23", font_size=48)
        subtitle = Text("Planos. Posiciones relativas", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Planos. Posiciones relativas":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
