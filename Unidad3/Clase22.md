

# 
  ### 
- Definir producto cruz entre vectores y sus propiedades.
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.

## Producto cruz
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase22.py Clase22` y mueva el archivo resultante a `_static/videos/Clase22.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase22.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  

Consideremos el siguiente problema: dados dos vectores no colineales $\vec{a}$ y $\vec{b}$ en el espacio, nos interesa obtener un tercer vector $\vec{c}$ que cumpla las siguientes condiciones: 
- $\vec{c}$ es perpendicular a $\vec{a}$. 
- $\vec{c}$ es perpendicular a $\vec{b}$.
    
  

```{admonition} Definición
:class: tip

Si $\vec{a}=(a_1,a_2,a_3)$ y $\vec{b}=(b_1,b_2,b_3)$ entonces el **producto cruz** de $\vec{a}$ y $\vec{b}$ es el vector  $$\color{red}\boxed{\color{black}\vec{a}\times\vec{b}=(a_2b_3-a_3b_2,a_3b_1-a_1b_3,a_1b_2-a_2b_1)}$$
```
   

A fin de hacer la definición más fácil de recordar, se usa la notación de determinantes.  Un **determinante de orden 2** se define mediante $$\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc.$$

Un **determinante de orden 3** se puede definir en términos de determinantes de segundo orden como sigue:  $$\begin{vmatrix}a&b&c\\a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}=a\begin{vmatrix}a_2&a_3\\b_2&b_3\end{vmatrix}-b\begin{vmatrix}a_1&a_3\\b_1&b_3\end{vmatrix}+c\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}.$$

## Propiedades
# (Untitled Slide)
  ## 
  ### 
  

Ahora, si definimos los vectores (**canónicos**) del espacio: $\hat{i}=(1,0,0)$, $\hat{j}=(0,1,0)$ y $\hat{k}=(0,0,1)$,  podemos reescribir el producto cruz de $\vec{a}$ con $\vec{b}$ como  
{$$\color{red}\boxed{\color{black}\vec{a}\times\vec{b}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}=\begin{vmatrix}a_2&a_3\\b_2&b_3\end{vmatrix}\hat{i}-\begin{vmatrix}a_1&a_3\\b_1&b_3\end{vmatrix}\hat{j}+\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}\hat{k}}$$} 

```{admonition} Ejemplo 1
:class: note

Determine el producto cruz de los vectores $\vec{a}=(1,1,1)$ y $\vec{b}=(-1,0,2)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

 

```{admonition} Propiedades
:class: tip

Sean $\vec{a},\vec{b}$ y $\vec{c}$ vectores en $\mathbb{R}^3$, y $\alpha$ un número real. Se verifican: 
[{(1)}]
- $\vec{a} \times \vec{b}$ es perpendicular a $\vec{a}$ y $\vec{b}$.
- $\vec{a} \times \vec{b}=-(\vec{b}\times \vec{a})$
- Si $\vec{a}$ y $\vec{b}$ son paralelos entonces $\vec{a}\times\vec{b}=\vec{0}$
- $\vec{a}\times (\alpha \vec{b})=(\alpha \vec{a})\times \vec{b}=\alpha ( \vec{a} \times \vec{b})$
- $\vec{a}\times (\vec{b}+\vec{c})=(\vec{a}\times \vec{b})+(\vec{a}\times \vec{c})$
- $||\vec{a} \times \vec{b}||$ es igual al área del parelelógramo formado por $\vec{a}$ y $\vec{b}$, y si $\theta$ es el ángulo formado por $\vec{a}$ y $\vec{b}$ entonces
$$||\vec{a} \times \vec{b}||=||\vec{a}||||\vec{b}||\sen(\theta).$$

```

# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Ejemplo 2
:class: note

Calcule el área del triángulo formado por los puntos $A(-1,2,3)$, $B(1,-2,0)$ y $C(2,4,5)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Nota
:class: tip

Si $\vec{a}$ y $\vec{b}$ son vectores del plano $XY$, entonces los podemos escribir como $\vec{a}=(a_1,a_2,0)$, $\vec{b}=(b_1,b_2,0)$ y  $$\vec{a}\times\vec{b}=0\hat{i}-0\hat{j}+\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}\hat{k}=(0,0,a_1b_2-a_2b_1)$$  que corresponde a un vector paralelo al eje $Z$.
```

    
```{admonition} Nota
:class: tip

$\vec{a}\times\vec{b}$ apunta en una dirección perpendicular a $\vec{a}$ y $\vec{b}$ que está dada por la **regla de la mano derecha**: si los dedos de su mano derecha se curvan en la dirección (en un ángulo menor que $\pi$) desde $\vec{a}$ hacia $\vec{b}$ entonces su dedo pulgar apunta en la dirección de $\vec{a}\times\vec{b}$.

\visible<6>{```{image} ../Clases/ProdCruz1.png
:align: center
:width: 70%
```}

```

  

  

  

  

  

  

