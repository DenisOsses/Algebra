# Instrucciones del Proyecto AlgebraBook

Este proyecto contiene el material del curso de Álgebra convertido para Jupyter Book.

## Estructura
- **Unidad X/**: Contienen las clases convertidas a Markdown.
- **scripts/**: Scripts de utilidad (conversión, generación de slides).
- **slides/**: Scripts de Python para generar las presentaciones con Manim.
- **_config.yml** y **_toc.yml**: Configuración del libro.

## Pasos para finalizar

### 1. Generar Animaciones (Opcional pero recomendado)
Para generar los videos de las presentaciones, necesitas tener instalado [Manim](https://docs.manim.community/en/stable/installation.html).

Ejecuta el siguiente comando para generar una clase (ej. Clase 01):
```bash
manim -pql slides/Clase01.py Clase01
```
Luego mueve el archivo de video resultante a `_static/videos/Clase01.mp4`.

### 2. Construir el Libro
Necesitas tener instalado Python y ejecutar:
```bash
python -m pip install jupyter-book ghp-import
```

Para construir el HTML:
```bash
jupyter-book build .
```
El resultado estará en `_build/html/index.html`.

### 3. Desplegar en GitHub Pages
Para subir los cambios y publicar:

```bash
# Agregar cambios
git add .
git commit -m "Actualización del libro"

# Subir al repositorio (asegúrate de tener permisos)
git push origin main

# Publicar en gh-pages
ghp-import -n -p -f _build/html
```

Una vez realizado esto, el libro estará disponible en `https://denisosses.github.io/Algebra/`.
