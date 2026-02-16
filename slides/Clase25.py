from manim import *

class Clase25(Scene):
    def construct(self):
        title = Text("Clase 25", font_size=48)
        subtitle = Text("Números complejos. Módulo, conjugado y forma polar.", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Números complejos. Módulo, conjugado y forma polar.":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
