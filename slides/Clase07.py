from manim import *

class Clase07(Scene):
    def construct(self):
        title = Text("Clases 7-8", font_size=48)
        subtitle = Text("Sucesiones. Principio de inducción. Ejemplos", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Sucesiones. Principio de inducción. Ejemplos":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
