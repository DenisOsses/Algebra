from manim import *

class Clase18(Scene):
    def construct(self):
        title = Text("Clase 18", font_size=48)
        subtitle = Text("Vectores en coordenadas. Norma", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Vectores en coordenadas. Norma":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
