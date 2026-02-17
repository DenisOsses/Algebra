import os
import re

SOURCE_DIR = "Clases"
OUTPUT_DIRS = {
    "Unidad1": range(1, 12),
    "Unidad2": range(12, 17),
    "Unidad3": range(17, 25),
    "Unidad4": range(25, 31)
}

def clean_tex_line(line):
    # Remove simple beamer commands
    line = re.sub(r'\\pause', '', line)
    line = re.sub(r'\\justifying', '', line)
    line = re.sub(r'\\footnotesize', '', line)
    line = re.sub(r'\\tiny', '', line)
    line = re.sub(r'\\small', '', line)
    line = re.sub(r'\\vspace\{.*?\}', '', line)
    line = re.sub(r'\\hspace\{.*?\}', '', line)
    line = re.sub(r'\\titleframe', '', line)
    line = re.sub(r'\\insertsectionhead', '', line)
    line = re.sub(r'\\insertsubsectionhead', '', line)
    line = re.sub(r'\\begin\{minipage\}.*', '', line)
    line = re.sub(r'\\end\{minipage\}', '', line)
    line = re.sub(r'\\linewidth', '', line)
    line = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', line)  # Convert bold
    line = re.sub(r'\\textit\{(.*?)\}', r'*\1*', line)    # Convert italic
    line = re.sub(r'%.*', '', line)  # Remove comments
    return line

def remove_ignored_frames(content):
    # Remove frames with specific titles
    # Titles: Temario, Objetivos, Objetivos de hoy, Contenidos
    ignore_patterns = [
        r'\\begin\{frame\}\{Temario\}.*?\\end\{frame\}',
        r'\\begin\{frame\}\{Objetivos.*?\}', # Open match, looking for closing?
        # Better: match the whole block with regex
    ]
    
    # Regex for frame with title
    # Note: .*? is non-greedy. flags=re.DOTALL needed.
    content = re.sub(r'\\begin\{frame\}\{(Temario|Objetivos|Objetivos de hoy|Contenidos|Tabla de contenidos)\}.*?\\end\{frame\}', '', content, flags=re.DOTALL)
    
    # Also remove separate \section{...} if they are just headers for these
    content = re.sub(r'\\section\{(Temario|Objetivos|Objetivos de hoy|Contenidos)\}', '', content)
    
    return content

def remove_preamble(content):
    if "\\begin{document}" in content:
        content = content.split("\\begin{document}")[1]
    if "\\end{document}" in content:
        content = content.split("\\end{document}")[0]
    return content

def convert_lists(content):
    # Convert itemize/enumerate to markdown lists
    # This is a bit simplistic but works for simple lists
    # Remove \begin{itemize/enumerate} and \end{...}
    content = re.sub(r'\\begin\{(itemize|enumerate)\}(\[.*?\])?', '', content)
    content = re.sub(r'\\end\{(itemize|enumerate)\}', '', content)
    # Convert \item
    content = re.sub(r'^\s*\\item\s+', '- ', content, flags=re.MULTILINE)
    return content

def remove_layout_commands(content):
    content = re.sub(r'\\begin\{minipage\}\{.*?\}', '', content)
    content = re.sub(r'\\end\{minipage\}', '', content)
    content = re.sub(r'\\begin\{columns\}', '', content)
    content = re.sub(r'\\end\{columns\}', '', content)
    content = re.sub(r'\\begin\{column\}\{.*?\}', '', content)
    content = re.sub(r'\\end\{column\}', '', content)
    content = re.sub(r'\\begin\{center\}', '', content)
    content = re.sub(r'\\end\{center\}', '', content)
    content = re.sub(r'\\begin\{multicols\}\{.*?\}', '', content)
    content = re.sub(r'\\end\{multicols\}', '', content)
    return content

def convert_admonitions(content):
    # Convert blocks to ```{admonition} style
    # \begin{block}{Title} -> ```{admonition} Title
    
    # Generic block to tip/note
    content = re.sub(
        r'\\begin\{block\}\{(.*?)\}',
        r'```{admonition} \1\n:class: tip',
        content
    )
    
    # Alert block to warning
    content = re.sub(
        r'\\begin\{alertblock\}\{(.*?)\}',
        r'```{admonition} \1\n:class: warning',
        content
    )
    
    # Example block to note
    content = re.sub(
        r'\\begin\{exampleblock\}\{(.*?)\}',
        r'```{admonition} \1\n:class: note',
        content
    )
    
    # Closing tags
    # We need to replace \end{block} etc with ```
    content = re.sub(r'\\end\{(block|alertblock|exampleblock)\}', '```', content)
    
    return content

def convert_structure(content):
    # Frames to headers
    # \begin{frame}{Title} -> # Title
    content = re.sub(r'\\begin\{frame\}\{(.*?)\}', r'# \1', content)
    content = re.sub(r'\\begin\{frame\}', r'# (Untitled Slide)', content)
    content = re.sub(r'\\frametitle\{(.*?)\}', r'## \1', content) # Subtitle or frametitle
    content = re.sub(r'\\framesubtitle\{(.*?)\}', r'### \1', content)
    content = re.sub(r'\\end\{frame\}', r'', content)
    
    # Sections
    content = re.sub(r'\\section\{(.*?)\}', r'# \1', content)
    content = re.sub(r'\\subsection\{(.*?)\}', r'## \1', content)
    
    return content

def convert_math(content):
    # Should work as is for most parts, mostly ensure consistency
    return content

def convert_images(content):
    # \includegraphics[scale=0.5]{image} -> ```{image} image.png \n :align: center```
    # We need to find the image file and path.
    # Assuming images are in the root or same dir.
    
    def repl(match):
        options = match.group(1)
        filename = match.group(2)
        # Check extensions
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            # Try to find the file
             for ext in ['.png', '.jpg', '.jpeg', '.pdf']:
                 if os.path.exists(os.path.join(SOURCE_DIR, filename + ext)):
                     filename += ext
                     break
        
        return f"```{{image}} ../Clases/{filename}\n:align: center\n:width: 70%\n```"

    content = re.sub(r'\\includegraphics\[(.*?)\]\{(.*?)\}', repl, content)
    content = re.sub(r'\\includegraphics\{(.*?)\}', lambda m: repl(re.match(r'\\includegraphics\[(.*?)\]\{(.*?)\}', f"\\includegraphics[]{m.group(1)}")), content)
    return content

def add_solution_toggles(content):
    lines = content.split('\n')
    new_lines = []
    in_example = False
    
    for line in lines:
        new_lines.append(line)
        if "```{admonition} Ejemplo" in line or "```{admonition} Ejercicio" in line:
            in_example = True
        
        if line.strip() == "```" and in_example:
            in_example = False
            new_lines.append("\n```{toggle} Solución")
            new_lines.append("*(Espacio para la solución detallada)*")
            new_lines.append("```\n")
            
    return '\n'.join(new_lines)

def process_file(filename, unit_path):
    with open(os.path.join(SOURCE_DIR, filename), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Conversions
    content = remove_preamble(content)
    content = remove_ignored_frames(content) # Filter before cleaning lines ideally
    
    # Pre-cleaning lines
    lines = content.split('\n')
    cleaned_lines = [clean_tex_line(l) for l in lines]
    content = '\n'.join(cleaned_lines)

    content = convert_structure(content)
    content = convert_admonitions(content)
    content = remove_layout_commands(content)
    content = convert_lists(content)
    content = convert_images(content)
    content = add_solution_toggles(content)
    
    # Final cleanup of double blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Final write
    output_filename = os.path.splitext(filename)[0].replace(' ', '') + ".md"
    with open(os.path.join(unit_path, output_filename), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted {filename} -> {os.path.join(unit_path, output_filename)}")

def main():
    files = sorted(os.listdir(SOURCE_DIR))
    for f in files:
        if not f.endswith('.tex'):
            continue
            
        # Determine Unit
        # logic: extract number from "Clase XX.tex"
        match = re.search(r'Clase\s*(\d+)', f)
        if match:
            num = int(match.group(1))
            target_unit = None
            for unit, r in OUTPUT_DIRS.items():
                if num in r:
                    target_unit = unit
                    break
            
            if target_unit:
                process_file(f, target_unit)
            else:
                print(f"Skipping {f} (No matching unit)")
        else:
            # Special handling for "Clase 07-08.tex" etc.
            if "07-08" in f: process_file(f, "Unidad1")
            elif "09-10" in f: process_file(f, "Unidad1")
            elif "21-2" in f: process_file(f, "Unidad3")
            else:
                print(f"Skipping {f} (Pattern not matched)")

if __name__ == "__main__":
    main()
