from manim import *

class Clase03(Scene):
    def construct(self):
        title = Text("Clase 3", font_size=48)
        subtitle = Text("Nociones de conjuntos. Funciones proposicionales", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Nociones de conjuntos. Funciones proposicionales":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
