from manim import *

class Clase20(Scene):
    def construct(self):
        title = Text("Clase 20", font_size=48)
        subtitle = Text("\small{Recta vectorial. Producto Punto y ortogonalidad. Posiciones relativas de rectas", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "\small{Recta vectorial. Producto Punto y ortogonalidad. Posiciones relativas de rectas":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
