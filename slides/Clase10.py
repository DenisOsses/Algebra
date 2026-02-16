from manim import *

class Clase10(Scene):
    def construct(self):
        title = Text("Clase 10", font_size=48)
        subtitle = Text("Sumas Dobles y Productorias", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Sumas Dobles y Productorias":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
