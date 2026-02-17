

# 
  ### 
- Representar algebraicamente vectores y sus operaciones.
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.

## Vectores en coordenadas
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase18.py Clase18` y mueva el archivo resultante a `_static/videos/Clase18.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase18.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  

```{admonition} Definición. Puntos en el plano
:class: tip

Cualquier punto $P$ en el plano puede localizarce por un único par ordenado $(a,b)$  

    \visible<2-4>{```{image} ../Clases/GeomVect1.png
:align: center
:width: 70%
```}

```

```{admonition} Definición
:class: tip

La **distancia entre los puntos** $P_1(x_1,y_1)$ y $P_2(x_2,y_2)$ es $$d(P_2,P_1)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.$$  

    \visible<4>{ ```{image} ../Clases/GeomVect2.png
:align: center
:width: 70%
```}

```

# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Definición. Puntos en el espacio
:class: tip

Cualquier punto $P$ en el espacio puede localizarce por un único trío de números $(a,b,c)$  

   \visible<2-6>{```{image} ../Clases/GeomVect3.png
:align: center
:width: 70%
```}
  
```
```{admonition} Ejemplo 1
:class: note
Localice los puntos $(2,4,7)$ y $(-4,3,-5)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

   \visible<4-6>{```{image} ../Clases/GeomVect4.png
:align: center
:width: 70%
```}
  

```{admonition} Definición
:class: tip

La **distancia entre los puntos del espacio** $P(x_1,y_1,z_1)$ y $Q(x_2,y_2,z_2)$ es $$d(Q,P)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.$$  

    \visible<6>{```{image} ../Clases/GeomVect5.png
:align: center
:width: 70%
```}

```

## Adición, ponderación y magnitud en coordenadas
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Definición
:class: tip

Todos los puntos $P(a,b)$ del plano y $P(a,b,c)$ del espacio tienen asociado un vector posición $$\vec{p}=(a,b)~~\text{o}~~\vec{p}=(a,b,c)$$  que corresponde a las **coordenadas** de dicho vector.  Esto es así porque podemos mirar todos los puntos $P$ desde el origen $O$ y asociarles su vector posición $\overrightarrow{OP}=\vec{p}$. 
```  

```{admonition} Definición
:class: tip

Sean $\vec{p_1}=(a_1,b_1,c_1)$ o $\vec{p_2}=(a_2,b_2,c_2)$ vectores del espacio. La **adición** de $\vec{p_1}$ y $\vec{p_2}$ en coordenadas es $$\vec{p_1}+\vec{p_2}=(a_1+a_2,b_1+b_2,c_1+c_2).$$ 
```

```{admonition} Definición
:class: tip

La **ponderación** del vector $\vec{p}=(a,b,c)$ por el escalar $\alpha\in\mathbb{R}$ en coordenadas es $$\alpha\vec{p}=\alpha(a,b,c)=(\alpha a,\alpha b,\alpha c).$$
```  

```{admonition} Definición
:class: tip

El **módulo** o **norma** del vector $\vec{p}=(a,b,c)$ es $$||\vec{p}||=\sqrt{a^2+b^2+c^2}.$$
```

## Distancia
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Propiedad
:class: tip

Si $\vec{u}$ es un vector en el plano o el espacio y $\alpha\in\mathbb{R}$, entonces: $$||\alpha\vec{u}||=|\alpha|\cdot||\vec{u}||.$$ 
```

```{admonition} Definición
:class: tip

Si $A$ y $B$ son puntos del plano o el espacio, y $\vec{a}$, $\vec{b}$ son sus vectores posición asociados entonces: $$d(A,B)=||\overrightarrow{AB}||=||\vec{b}-\vec{a}||$$   es la **distancia** entre $A$ y $B$, o la norma del vector $\overrightarrow{AB}$. 
```
 

```{admonition} Ejemplo 2
:class: note

Obtener las coordenadas del vector $\overrightarrow{AB}$ determinado por un punto inicial $A(3,2)$ y un punto final $B(-5,1)$. ¿Cuáles son las coordenadas del punto $D$ si $\overrightarrow{CD}=\overrightarrow{AB}$ con $C(-4,7)$?
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  

  

  

  

  

  

