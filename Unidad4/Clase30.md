

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase30.py Clase30` y mueva el archivo resultante a `_static/videos/Clase30.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase30.mp4" type="video/mp4">
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
- Definir polinomios junto a sus elementos y operaciones principales.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Polinomios
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Definición
:class: tip

Un polinomio $f$ es una expresión (función) de la forma $$f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots a_2x^2+a_1x+a_0~~,~~x\in\mathbb{R}$$ donde los $a_i\in\mathbb{R}$ se denominan \textbf{coeficientes} del polinomio y $n\in\mathbb{N}$ es su \textbf{grado} u \textbf{orden}.
:::

% :::{admonition} Ejemplo
:class: note
% 
% Las funciones constante, lineal, cuadrática y cúbica son polinomios.
% :::

:::{admonition} Definición
:class: tip

Un polinomio $f$ es \textbf{divisible} por el polinomio $p$ si existe otro polinomio $q$ tal que $$f(x)=p(x)q(x).$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo
:class: note

$x^4-16$ es divisible por $x^2-4$, $x^2+4$, $(x-2)$ y $x+2$, pero no es divisible por $x^2+3x+1.$
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} División de polinomios
:class: tip

Si $f(x)$ y $p(x)$ son polinomios y si $p(x)\neq0$, entonces existen polinomios únicos $q(x)$ y $r(x)$ tales que $$f(x)=p(x)q(x)+r(x)$$
donde ya sea $r(x)=0$ o el grado de $r(x)$ es menor que el grado de $p(x)$. El polinomio $q(x)$ es el \textbf{cociente} y $r(x)$ es el \textbf{residuo} en la división de $f(x)$ entre $p(x)$.
:::





%---------------------------------------------------------------------
## Teorema del Resto
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo
:class: note

Realice la división de $x^4-16$ entre $x^2+3x+1.$
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

:::{admonition} Teorema del Resto
:class: tip

Si un polinomio $f(x)$ se divide entre $x-c$, entonces el residuo (resto) es $f(c)$
::: 

:::{admonition} Teorema del Factor
:class: tip

Un polinomio $f(x)$ tiene un factor $x-c$ si y sólo si $f(c)=0$.
:::
 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo
:class: note

Demuestre que $x-2$ es un factor del polinomio $~~~~f(x)=x^3-4x^2+3x+2$.
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


Para aplicar el teorema del resto es necesario dividir un polinomio $f(x)$ entre $x-c$. El método de \textbf{división sintética} se puede usar para simplificar este
trabajo.  

:::{admonition} Ejemplo
:class: note

Use división sintética para hallar el cociente $q(x)$ y residuo $r$ si el polinomio $2x^4+5x^3-2x-8$ se divide entre $x+3$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::






%---------------------------------------------------------------------
## División Sintética
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

    ```{image} ../Clases/sintetica.png
:align: center
:width: 70%
```

 
\begin{minipage}[t]{0.5\linewidth}

Los teoremas del factor y el resto se pueden extender al conjunto de números complejos. Así, un número complejo $c=a+bi$ es un cero de un polinomio $f(x)$ si y sólo si $x-c$ es un factor de $f(x)$. Excepto en casos especiales,
los ceros de polinomios son muy difíciles de hallar. El siguiente teorema expresa que hay al menos un cero $c$ y, en consecuencia, por el teorema del factor, $f(x)$ tiene un factor de la forma $x-c$.




%---------------------------------------------------------------------
## Teorema Fundamental del Álgebra
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Teorema Fundamental del Álgebra
:class: tip

    Si un polinomio $f(x)$ tiene un grado positivo y coeficientes complejos, entonces $f(x)$ tiene al menos un cero complejo.
::: 
\begin{block}{Factorización
completa para polinomios}

Si $f(x)$ es un polinomio de grado $n>0$, entonces existen $n$ números complejos $c_1,c_2,\ldots,c_n$ tales que $$f(x)=a(x-c_1)(x-c_2)\cdots(x-c_n)$$
donde $a$ es el coeficiente principal de $f(x)$. Cada número $c_k$ es un cero de $f(x).$
:::
 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo
:class: note
     Factorice completamente el polinomio $$p(x)=5x^3-30x^2+65x$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Teorema
:class: tip
    
    Todo polinomio con coeficientes reales y $n$ de grado positivo se pueden expresar como un producto de polinomios lineales y cuadráticos con coeficientes reales tales que los factores cuadráticos son irreducibles sobre $\mathbb{R}$.
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


