from manim import *

class Clase16(Scene):
    def construct(self):
        title = Text("Clase 16", font_size=48)
        subtitle = Text("Teoremas del seno y del coseno", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Teoremas del seno y del coseno":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
