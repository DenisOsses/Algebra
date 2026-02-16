from manim import *

class Clase15(Scene):
    def construct(self):
        title = Text("Clase 15", font_size=48)
        subtitle = Text("Funciones inversas y Ecuaciones trigonométricas.", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Funciones inversas y Ecuaciones trigonométricas.":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
