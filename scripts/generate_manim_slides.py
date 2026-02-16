import os
import re

SOURCE_DIR = "Clases"
SLIDES_DIR = "slides"

TEMPLATE = """from manim import *

class Clase{num}(Scene):
    def construct(self):
        title = Text("{title}", font_size=48)
        subtitle = Text("{subtitle}", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        if "{subtitle}":
            self.play(Write(subtitle))
            self.wait(2)
        
        # Add more content here based on the class topics
        self.wait(2)
"""

def extract_metadata(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex for title/subtitle. Might need adjustment if they span multiple lines.
    title_match = re.search(r'\\title\{(.*?)\}', content)
    subtitle_match = re.search(r'\\subtitle\{(.*?)\}', content)
    
    title = title_match.group(1) if title_match else "Clase sin título"
    # Remove math inside title for simplicity or handle it? Text object supports basic text.
    # Tex object supports LaTeX. Let's use Tex for better support.
    # But for now Text is safer for unknown chars.
    
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    return title, subtitle

def main():
    if not os.path.exists(SLIDES_DIR):
        os.makedirs(SLIDES_DIR)
        
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith(".tex"): continue
        
        # Extract number
        num_match = re.search(r'Clase\s*(\d+)', filename)
        if not num_match: 
            # Try to handle 07-08 etc
            continue
        num = num_match.group(1)
        
        title, subtitle = extract_metadata(os.path.join(SOURCE_DIR, filename))
        
        # Clean title/subtitle for python string
        title = title.replace('"', '\\"').replace('\n', ' ')
        subtitle = subtitle.replace('"', '\\"').replace('\n', ' ')
        
        # Write slide file
        with open(os.path.join(SLIDES_DIR, f"Clase{num}.py"), "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(num=num, title=title, subtitle=subtitle))
            
    print("Slides generated in", SLIDES_DIR)

if __name__ == "__main__":
    main()
