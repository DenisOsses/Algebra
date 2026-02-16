from manim import *

class Clase12(Scene):
    def construct(self):
        title = Text("Clase 12", font_size=48)
        subtitle = Text("Razones trigonométricas en triángulos rectángulos", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "Razones trigonométricas en triángulos rectángulos":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
