from manim import *

class Clase04(Scene):
    def construct(self):
        title = Text("Clase 4", font_size=48)
        subtitle = Text("Álgebra de funciones proposicionales", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Álgebra de funciones proposicionales":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
