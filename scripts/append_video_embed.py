import os
import re

SLIDES_DIR = "slides"
# Note: Ensure _static exists
CONTENT_DIRS = ["Unidad1", "Unidad2", "Unidad3", "Unidad4"]

def main():
    if not os.path.exists("_static"):
        os.makedirs("_static")
    if not os.path.exists("_static/videos"):
        os.makedirs("_static/videos")
        
    for slide_file in os.listdir(SLIDES_DIR):
        if not slide_file.endswith(".py"): continue
        
        num_match = re.search(r'Clase(\d+)', slide_file)
        if not num_match: continue
        num = num_match.group(1)
        
        # Find the content file
        target_file = None
        for d in CONTENT_DIRS:
            # Match ClaseXX.md or ClaseXX-YY.md
            if not os.path.exists(d): continue
            for f in os.listdir(d):
                # Robust matching for Clase01 vs Clase1 etc
                # If f starts with Clase{num} (padded or not?)
                # My filenames are Clase01.md, Clase10.md.
                # num from slide file is '01' or '10'.
                if f.startswith(f"Clase{num}") and f.endswith(".md"):
                    target_file = os.path.join(d, f)
                    break
            if target_file: break
        
        if target_file:
            print(f"Adding video embed to {target_file}")
            with open(target_file, "r+", encoding="utf-8") as f:
                content = f.read()
                # Check if already added
                if "video-container" in content:
                    print("Video already embedded.")
                    continue
                

                embed_code = (
                    f"\n:::" + "{admonition} Presentación de la Clase\n"
                    f":class: note\n"
                    f"Para generar el video, ejecute: `manim -pql slides/Clase{num}.py Clase{num}` y mueva el archivo resultante a `_static/videos/Clase{num}.mp4`.\n"
                    f":::\n\n"
                    f'<div class="video-container" style="text-align: center; margin-bottom: 2em;">\n'
                    f'  <video width="80%" controls>\n'
                    f'    <source src="../_static/videos/Clase{num}.mp4" type="video/mp4">\n'
                    f'    Tu navegador no soporta el elemento video.\n'
                    f'  </video>\n'
                    f'</div>\n'
                )
                # Insert after the first header block
                f.seek(0)
                lines = f.readlines()
                insert_idx = len(lines) # Default append
                
                # Logic: Find first # and potentially ##
                found_header = False
                for i, line in enumerate(lines):
                    if line.strip().startswith("# "):
                        insert_idx = i + 1
                        found_header = True
                        # Look ahead for subtitle
                        if i+1 < len(lines) and lines[i+1].strip().startswith("## "):
                             insert_idx = i + 2
                        break
                
                if not found_header:
                    insert_idx = 0

                lines.insert(insert_idx, embed_code)
                f.seek(0)
                f.write("".join(lines))
        else:
            print(f"Content file for {slide_file} not found.")

if __name__ == "__main__":
    main()
