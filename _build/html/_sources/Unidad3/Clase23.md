

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase23.py Clase23` y mueva el archivo resultante a `_static/videos/Clase23.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase23.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  \setbeamertemplate{section in toc}[sections numbered]
  \tableofcontents%[hideallsubsections]


%==============================================
# Objetivos de hoy
%==============================================
%## Charts
# \insertsectionhead
  ### \insertsubsectionhead
- Reconocer los elementos de las diferentes representaciones de planos y determinar sus ecuaciones.
- Usar las distintas representaciones de planos y sus propiedades para resolver problemas geométricos.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Planos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
Observemos la siguiente figura:

```{image} ../Clases/Plano1.png
:align: center
:width: 70%
```

 
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Un \textbf{plano} en el espacio $\mathbb{R}^3$ es el conjunto determinado por 
- un punto $P_0(x_0, y_0, z_0)$ en el plano
- y un vector $\vec{n}$ que es ortogonal al plano. Este vector ortogonal $\vec{n}$ se llama \textbf{vector normal}.
 

Sea $P(x, y, z)$ un punto arbitrario en el plano, y sean $\vec{r}_0$ y $\vec{r}$ los vectores posición de $P_0$ y $P$, respectivamente.  Entonces $\overrightarrow{P_0P}=\vec{r}-\vec{r}_0$.  El vector normal $\vec{n}$ es ortogonal a todo vector en el plano dado.  En particular, $\vec{n}$ es ortogonal a $\vec{r}-\vec{r}_0$, por tanto, se tiene   $$\color{red}\boxed{\color{black}\vec{n}\cdot(\vec{r}-\vec{r}_0)=0}.$$ 
Esta ecuación es conocida como \textbf{ecuación vectorial del plano}.

:::





%---------------------------------------------------------------------
%## Planos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
Si escribimos los vectores en coordenadas: $\vec{n}=(a,b,c)$, $\vec{r}=(x,y,z)$ y $\vec{r}_0=(x_0,y_0,z_0)$.  Reemplazando en la ecuación vectorial, obtenemos $$(a,b,c)\cdot(x-x_0,y-y_0,z-z_0)=0.$$  Equivalentemente, $$\color{red}\boxed{\color{black}a(x-x_0)+b(y-y_0)+c(z-z_0)=0}$$ 
que es conocida como \textbf{ecuación general del plano} que contiene al punto $P_0(x_0,y_0,z_0)$ con vector normal $\vec{n}$. 
:::{admonition} Nota
:class: tip

Un plano que contiene al punto $P_0(x_0,y_0,z_0)$ es generado por 2 vectores no paralelos $\vec{u}$ y $\vec{v}$, cuya ecuación es $\vec{r}=\vec{r}_0+\mu\vec{u}+\lambda\vec{v}$, con $\mu,\lambda\in\mathbb{R}$.
:::

 
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 1
:class: note

Determine la ecuación del plano que pasa por los puntos $A(1,1,-1)$, $B(2,-1,3)$ y $C(3,1,1)$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

:::{admonition} Nota
:class: tip

En el ejemplo anterior reescribimos la ecuación del plano como $$\color{red}\boxed{\color{black}ax+by+cz=d}$$
Esta ecuación es conocida como \textbf{ecuación cartesiana del plano} y es la forma habitual de escribirla.

Además, si 2 de los 3 parámetros $a,b,c$ son 0, entonces tenemos \textbf{planos paralelos a los planos coordenados} $XY$, $XZ$ e $YZ$. 
:::




%---------------------------------------------------------------------
## Posiciones relativas entre planos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Dos planos son \textbf{paralelos} si sus vectores normales son paralelos.  Dos planos son \textbf{ortogonales o perpendiculares} si sus vectores normales son ortogonales o perpendiculares. 
:::
:::{admonition} Ejemplo 2
:class: note

Encuentre la ecuación del plano $\pi$ sabiendo que:
- $(0, 0, 0)\in\pi$,
- $\pi$ es perpendicular al plano $\pi_1$, donde $\pi_1: x + y - z = 1$,
- $\pi$ es paralelo a la recta $\ell$, donde $\ell : x = -1 -3, y = 1 + 2t, z = t$, con $t$ en $\mathbb{R}$.

:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}

   \visible<4-5>{```{image} ../Clases/Plano2.png
:align: center
:width: 70%
```}

:::{admonition} Definición
:class: tip

El ángulo $\theta$ entre dos planos $\pi_1$ y $\pi_2$ corresponde al ángulo formado por sus vectores normales $\vec{n}_1$ y $\vec{n}_2$, respectivamente.
:::




%---------------------------------------------------------------------
%## Posiciones relativas entre planos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo 3
:class: note

Considere el punto $P(2,0,1)$ y la recta $$L:(x,y,z)=(1,2,3)+t(-2,-1,1)~~,~~t\in\mathbb{R}.$$
- Encuentre la ecuación del plano que contiene al punto $P$ y es perpendicular a $L$.
- Encuentre la ecuación del plano que contiene a la recta $L$ y al punto $P$.

:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}






% %==============================================
% # Conclusión
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   
%   
%       \item Advierta que la ecuación $ax+by=d$ representa un plano en el espacio, no una recta en el plano. Cada ecuación debe ser entendida en su contexto. 
%   

% 


% %==============================================
% # Asistencia
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   \textbf{Solo se considerará la asistencia hasta 5 minutos después de terminada la clase.}
  
%   
%   ```{image} ../Clases/QR
:align: center
:width: 70%
```
%   
  
% 


