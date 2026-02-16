from manim import *

class Clase02(Scene):
    def construct(self):
        title = Text("Clase 2", font_size=48)
        subtitle = Text("Equivalencias Lógicas. Álgebra proposicional", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Equivalencias Lógicas. Álgebra proposicional":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
