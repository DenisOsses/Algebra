

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase25.py Clase25` y mueva el archivo resultante a `_static/videos/Clase25.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase25.mp4" type="video/mp4">
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
- Utilizar las distintas representaciones de los números complejos y sus operaciones.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Números complejos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

Algunas ecuaciones cuadráticas no tienen
solución real. Por ejemplo $x^2+1=0$ no tiene raíces reales porque no existe $x\in\mathbb{R}$ tal que $x^2=-1$.



Para resolver todas las ecuaciones cuadráticas, se crea un sistema numérico expandido llamado conjunto de \textbf{números complejos} $\mathbb{C}$, en el cual se define el número \textbf{imaginario} $i$ con la propiedad que $$i^2=-1~~\Leftrightarrow~~i=\sqrt{-1}.$$

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Un \textbf{número complejo} es una expresión de la forma $$z=a+bi$$
donde $a$ y $b$ son números reales y $i^2=-1$. La \textbf{parte real} de este número complejo es $a$ y la \textbf{parte imaginaria} es $b$.  
Dos números complejos son iguales si y solo si sus partes reales son iguales y sus partes imaginarias son iguales. 


El número complejo $a+bi$ también puede estar representado por el par ordenado $(a,b)$ y determinado como un punto en un plano (llamado plano de Argand) como en la figura siguiente.  De este modo, el número complejo $i=0+1\cdot i$ se identifica con el punto $(0,1)$.
:::




%---------------------------------------------------------------------
## Álgebra y operaciones de números complejos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

    ```{image} ../Clases/Complejo1.png
:align: center
:width: 70%
```


:::{admonition} Definición
:class: tip

La parte real del complejo $z=a+bi$ se anota como $Re(z)=a$ y la parte imaginaria como $Im(z)=b$.  Note que $Re(z), Im(z)\in\mathbb{R}$.  A partir de esto, el eje horizontal del plano de Argand se denomina \textbf{eje real} y el eje vertical se llama \textbf{eje imaginario}.
:::

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Si $z=a+bi$ y $w=c+di$ entonces 

[{(1)}]
- su \textbf{adición} está dada por: $z+w=(a+c)+(b+d)i$.
- su \textbf{resta} está dada por: $z-w=(a-c)+(b-d)i$.
- su \textbf{producto} está dado por: $zw=(ac-bd)+(bc+ad)i$.
- su \textbf{división} está dada por: $\dfrac{z}{w}=\dfrac{(ac+bd)+(bc-ad)i}{c^2+d^2}$.
- el \textbf{módulo} de $z$ está dado por: $|z|=\sqrt{a^2+b^2}$.
- el \textbf{conjugado} de $z$ está dado por: $\overline{z}=a-bi$.

:::




%---------------------------------------------------------------------
%## Álgebra y operaciones de números complejos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

```{image} ../Clases/Complejo2.png
:align: center
:width: 70%
```
% \captionof{figure}{Conjugación}


```{image} ../Clases/Complejo3.png
:align: center
:width: 70%
```
% \captionof{figure}{Módulo}


:::{admonition} Propiedades
:class: tip

Si $z=a+bi$ y $w=c+di$ entonces 

[{(a)}]
- $z\overline{z}=|z|^2$
- $\dfrac{z}{w}=\dfrac{z\overline{w}}{|w|^2}$
- $\overline{z+w}=\overline{z}+\overline{w}$
- $\overline{zw}=\overline{z}\;\overline{w}$
- $z+\overline{z}=2Re(z)$
- $z-\overline{z}=2iIm(z)$


:::

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 1
:class: note

Dados los números complejos $z_1=\frac{1}{4}+\frac{2}{3}i$ y $z_1=\frac{1}{8}+\frac{1}{6}i$, calcule
- $z_1+z_2$
- $|z_1-z_2|$
- $z_1:z_2$
- $\bar{z_1}\cdot z_2$


::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 2
:class: note

Determine la parte real e imaginaria de los siguientes números complejos


%\item $\dfrac{1}{2+i}$
- $\dfrac{3+2i}{3-2i}$
- $(1+i)^4$
- $\dfrac{8}{(1-i)^5}$


:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





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

Si $z=a+bi$, entonces su \textbf{forma polar} es $$z=r(\cos(\theta)+i\sen(\theta))$$  donde $r=|z|=\sqrt{a^2+b^2}$ y $\tan(\theta)=\frac{b}{a}$.  El ángulo $\theta$ se llama \textbf{argumento} de $z$ y escribimos $\theta=\arg(z)$.  Note que $\arg(z)$ no es único.
:::

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 3
:class: note

Calcule el m\'odulo y el argumento de los n\'umeros $\dfrac{1+i}{1-i}$ y $\dfrac{\sqrt{2}}{1-i}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

:::{admonition} \color{red
:class: noteEjercicio Propuesto}


Escriba en forma polar el n\'umero complejo $\dfrac{i^5-i^{-4}}{-\sqrt{2}i}$
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
%       \item Los números complejos son una extensión de los números reales, pero no poseen orden: no podemos decir si un complejo es positivo o negativo. 
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


