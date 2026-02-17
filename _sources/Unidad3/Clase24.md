

# 
  ### 
- Calcular distancias entre puntos, rectas y planos.

## Distancia Punto-Plano
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase24.py Clase24` y mueva el archivo resultante a `_static/videos/Clase24.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase24.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  

Queremos determinar la distancia $D$ (más corta) entre el punto $P_1(x_1,y_1,z_1)$ y el plano $\pi: ax+by+cz=d$  

\visible<2-10>{```{image} ../Clases/distancia1.png
:align: center
:width: 70%
```}
 

Para ello, elegimos cualquier punto $P_0(x_0,y_0,z_0)$ del plano y construimos el vector $\vec{b}=\overrightarrow{P_0P_1}$.  Luego lo proyectamos sobre el vector $\vec{n}=(a,b,c)$ normal al plano:

$D=||P_{\vec{n}}(\vec{b})||=\left|\left|\left(\frac{\vec{b}\cdot\vec{n}}{||\vec{n}||^2}\right)\vec{n}\right|\right|=\frac{|\vec{b}\cdot\vec{n}|}{||\vec{n}||^2}||\vec{n}||$ Por tanto, 

$\color{red}\boxed{\color{black}D=\frac{|\vec{b}\cdot\vec{n}|}{||\vec{n}||}}$

Esta expresión corresponde a la **distancia** $D$ **en forma vectorial**
 

Podemos expresar esta fórmula reemplazando $\vec{b}=(x_1-x_0,y_1-y_0,z_1-z_0)$, $\vec{n}=(a,b,c)$ y simplificando:  $$\color{red}\boxed{\color{black}D=\frac{|ax_1+by_1+cz_1-d|}{\sqrt{a^2+b^2+c^2}}}$$

```{admonition} Ejemplo 1
:class: note

Determine la distancia del punto $B(1,-2,3)$ al plano $2x-y-z=2$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

## Distancia Punto-Recta
# (Untitled Slide)
  ## 
  ### 
  

Queremos determinar la distancia $D$ (más corta) entre el punto $P_1(x_1,y_1,z_1)$ y la recta $L: \vec{r}=\vec{p}_0+\lambda\vec{v}$, $\lambda\in\mathbb{R}$.

\begin{figure} [h]
\centering
\visible<2-7>{```{image} ../Clases/distancia2.png
:align: center
:width: 70%
```}
\end{figure}

Para ello elegimos cualquier punto $P_0(x_0,y_0,z_0)$ de la recta y construimos el vector $\vec{b}=\overrightarrow{P_0P_1}$.  Luego lo proyectamos sobre el vector director $\vec{v}$ de la recta $L$, obteniendo $P_{\vec{v}}(\vec{b})$.  Notamos que $$P_{\vec{v}}(\vec{b})+\vec{y}=\vec{b}~~\Rightarrow~~\vec{y}=\vec{b}-P_{\vec{v}}(\vec{b}).$$  Como $$D=||\vec{y}||$$ concluimos que $$\color{red}\boxed{\color{black}D=\left|\left|\vec{b}-P_{\vec{v}}(\vec{b})\right|\right|}$$ 
Note que $D$ corresponde a la norma (longitud) del vector complemento ortogonal de $\vec{b}$ sobre $\vec{v}$.

# (Untitled Slide)
  ## 
  ### 
  

Otra forma de determinar la distancia $D$ desde el punto $P_1$ a la recta $L$ es mediante el siguiente proceso:  Tenemos que $$P_{\vec{v}}(\vec{b})+\vec{y}=\vec{b}$$  Hacemos producto cruz $\times$ de esta igualdad con $\vec{v}$.  Obtenemos $$P_{\vec{v}}(\vec{b})\times\vec{v}+\vec{y}\times\vec{v}=\vec{b}\times\vec{v}.$$ Como $\vec{v}$ y $P_{\vec{v}}(\vec{b})$ son paralelos entonces $P_{\vec{v}}(\vec{b})\times\vec{v}=\vec{0}$.  Así $\vec{y}\times\vec{v}=\vec{b}\times\vec{v}.$  Ahora tomamos la norma de estos vectores  $$||\vec{y}\times\vec{v}||=||\vec{b}\times\vec{v}||~~\Rightarrow~~||\vec{y}||\cdot||\vec{v}||\sen\left(\frac{\pi}{2}\right)=||\vec{b}\times\vec{v}||.$$
Por lo tanto

 $$\color{red}\boxed{\color{black}D=\frac{||\vec{b}\times\vec{v}||}{||\vec{v}||}}$$ 

```{admonition} Ejemplo 2
:class: note

Determine la distancia desde el punto $A(1,2,3)$ a la recta \begin{eqnarray*}x&=&2t\\ y&=&-1-t~~,~~t\in\mathbb{R} \\ z&=&3\end{eqnarray*}
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} \color{red
:class: note{Ejercicio Propuesto}}

Determine una fórmula que permita calcular la distancia más corta entre las rectas de ecuaciones $\ell_1: \vec{r}_1=\vec{p}_1+t_1\vec{v}_1$, $t_1\in\mathbb{R}$ y $\ell_2: \vec{r}_2=\vec{p}_2+t_2\vec{v}_2$, $t_2\in\mathbb{R}$.
```

  

  

  

  

  

  

