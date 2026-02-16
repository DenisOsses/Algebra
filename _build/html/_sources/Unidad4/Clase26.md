

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase26.py Clase26` y mueva el archivo resultante a `_static/videos/Clase26.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase26.mp4" type="video/mp4">
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
- Representar un complejo en forma polar.
- Interpretar geométrica y algebraicamente las raíces $n$-ésimas de números complejos.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Forma polar
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

    ```{image} ../Clases/Complejo4.png
:align: center
:width: 70%
```
 
:::{admonition} Definición
:class: tip

Si $z=a+bi$, entonces su \textbf{forma polar} es $$z=r(\cos(\theta)+i\sen(\theta))=r\textrm{cis}(\theta)$$  donde $r=|z|=\sqrt{a^2+b^2}$ y $\tan(\theta)=\frac{b}{a}$.  El ángulo $\theta$ se llama \textbf{argumento} de $z$ y escribimos $\theta=\arg(z)$.  Note que $\arg(z)$ no es único.
:::

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 1
:class: note

Calcule el m\'odulo y el argumento de $\dfrac{1+i}{1-i}$ 
% y $\dfrac{\sqrt{2}}{1-i}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

% :::{admonition} \color{red
:class: noteEjercicio Propuesto}
% 
% 
% Escriba en forma polar el n\'umero complejo $\dfrac{i^5-i^{-4}}{-\sqrt{2}i}$
% :::






%---------------------------------------------------------------------
## Multiplicación en forma polar y Teorema de De Moivre
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

    ```{image} ../Clases/Complejo5.png
:align: center
:width: 70%
```

La forma polar de números complejos da idea de la multiplicación y la división.  Si $z_1=r_1(\cos(\theta_1)+i\sen(\theta_1))$ y $z_2=r_2(\cos(\theta_2)+i\sen(\theta_2))$ entonces  $$\color{red}\boxed{\color{black}z_1z_2=r_1r_2(\cos(\theta_1+\theta_2)+i\sen(\theta_1+\theta_2))}$$

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Teorema (De Moivre)
:class: tip

Si $z=r(\cos(\theta)+i\sen(\theta))$ y $n\in\mathbb{N}$ entonces  $$z^n=r^n(\cos(n\theta)+i\sen(n\theta)).$$
::: 
:::{admonition} Ejemplo 2
:class: note

Calcule $(1+i)^{100}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





%---------------------------------------------------------------------
## Raíces $n$-ésimas de un complejo
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
El teorema de De Moivre también se puede usar para hallar las raíces $n$-ésimas de
números complejos.  

:::{admonition} Definición
:class: tip

Una raíz $n$-ésima del número complejo $z$ es un número complejo $w$ tal que $w^n=z$.
::: 

:::{admonition} Teorema
:class: tip

Sea $z=r(\cos(\theta)+i\sen(\theta))$ y $n\in\mathbb{N}$. Entonces $z$ tiene las $n$ raíces distintas $$w_k=r^{1/n}\left[\cos\left(\frac{\theta+2k\pi}{n}\right)+i\sen\left(\frac{\theta+2k\pi}{n}\right)\right]$$ para $k=0,1,2,\ldots,n-1.$
::: 

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Nota
:class: tip

Las raíces $n$-ésimas de $z$ tienen módulo $|w_k|=r^{1/n}$, es decir, $w_k$ se ubican en el círculo de radio $r^{1/n}$ del plano complejo.  También,
como el argumento de cada raíz sucesiva $w_k$ excede al argumento de la raíz previa en
$2\pi/n$, estas se encuentran igualmente espaciadas en este círculo.  Ver \href{https://www.geogebra.org/m/bterebwm}{\textbf{Geogebra}}
::: 

:::{admonition} Ejemplo 3
:class: note

Calcule las raíces sextas de $-8$.
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 4
:class: note

Determine las soluciones complejas de $z^4-i=0$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





% %==============================================
% # Conclusión
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   
%   
%       \item Desde el punto de vista polar, la multiplicación de complejos se puede interpretrar como rotaciones.
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


