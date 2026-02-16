from manim import *

class Clase30(Scene):
    def construct(self):
        title = Text("Clase 27", font_size=48)
        subtitle = Text("Polinomios. Algoritmo de la División y Teorema del Resto", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Polinomios. Algoritmo de la División y Teorema del Resto":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
