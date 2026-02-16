from manim import *

class Clase09(Scene):
    def construct(self):
        title = Text("Clase 9", font_size=48)
        subtitle = Text("Principio de inducción. Ejemplos", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Principio de inducción. Ejemplos":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
