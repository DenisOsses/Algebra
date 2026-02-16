from manim import *

class Clase19(Scene):
    def construct(self):
        title = Text("Clase 19", font_size=48)
        subtitle = Text("Combinación lineal. Vectores paralelos. Producto Punto", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Combinación lineal. Vectores paralelos. Producto Punto":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
