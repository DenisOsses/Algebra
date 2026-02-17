

# 
  ### 
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.
- Definir los conceptos de paralelismo entre vectores y producto punto.
    

## Combinación lineal
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase19.py Clase19` y mueva el archivo resultante a `_static/videos/Clase19.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase19.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  

```{admonition} Definición
:class: tip

Un vector $\vec{v}$ es **combinación lineal** de los vectores $\vec{u_1}$ y $\vec{u_2}$ si existen contantes $\alpha,\beta\in\mathbb{R}$ tales que $$\vec{v}=\alpha\vec{u_1}+\beta\vec{u_2}.$$
```

```{admonition} Ejemplo 1
:class: note

Sean $\vec{u}=(3,1)$ y $\vec{v}=(1,2)$. Determine si el vector $\vec{w}=(-1,3)$ es combinación lineal de $\vec{u}$ y $\vec{v}$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

   \visible<3>{```{image} ../Clases/Vect1.png
:align: center
:width: 70%
```}

## Vectores paralelos
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Definición
:class: tip

Decimos que los vectores $\vec{u}$ y $\vec{v}$ son **paralelos** si tienen la misma dirección.  Matemáticamente esto significa que un vector es un ponderado o múltiplo del otro, es decir, existe un número $\lambda\in\mathbb{R}$, $\lambda\neq0$, tal que $$\vec{u}=\lambda\vec{v}.$$
```

```{admonition} Ejemplo 2
:class: note
Decida si los vectores $\vec{u}=(-1,2)$ y $\vec{v}=(4,-8)$ son paralelos o no.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

## Producto punto
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Definición
:class: tip

Sean $\vec{a}=(a_1,a_2,a_3)$ y $\vec{b}=(b_1,b_2,b_3)$ vectores en el espacio.  El **producto punto** o **producto escalar** de $\vec{a}$ con $\vec{b}$ es el número real $\vec{a}\cdot\vec{b}$ definido por  $$\vec{a}\cdot\vec{b}=a_1b_1+a_2b_2+a_3b_3=\sum_{i=1}^3a_ib_i.$$
``` 
Así, para encontrar el producto punto de $\vec{a}$ con $\vec{b}$ se multiplican las coordenadas correspondientes y se suman.  El resultado no es un vector, es un número real.  
```{admonition} Ejemplo 3
:class: note

Calcule el producto punto entre $\vec{a}=(1,2,3)$ y $\vec{b}=(-1,0,1)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

 

```{admonition} Propiedades
:class: tip
 Si $\vec{a}$, $\vec{b}$ y $\vec{c}$ son vectores en el plano o en el espacio y $\alpha\in\mathbb{R}$, entonces 
[{(a)}]
- $\vec{a}\cdot\vec{a}=||\vec{a}||^2$.
- $\vec{a}\cdot \vec{b}=\vec{b} \cdot \vec{a}$.
- $\vec{a}\cdot (\vec{b}+\vec{c})=\vec{a}\cdot \vec{b}+\vec{a}\cdot \vec{c}$.
- $\alpha(\vec{a}\cdot \vec{b})=(\alpha \vec{a})\cdot \vec{b}=\vec{a}\cdot (\alpha \vec{b})$.
- $\vec{0}\cdot\vec{a}=0$.
- $\vec{a}\cdot \vec{b}=\frac{1}{2}( ||\vec{a}||^2+||\vec{b}||^2-||\vec{b}-\vec{a}||^2)$

```

  

  

  

  

  

  

  

  

  

