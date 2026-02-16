from manim import *

class Clase26(Scene):
    def construct(self):
        title = Text("Clase 26", font_size=48)
        subtitle = Text("Forma Polar de un complejo. Potencias y Raíces $n$-ésimas", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Forma Polar de un complejo. Potencias y Raíces $n$-ésimas":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
