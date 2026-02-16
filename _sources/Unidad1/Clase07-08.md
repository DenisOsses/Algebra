

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase07.py Clase07` y mueva el archivo resultante a `_static/videos/Clase07.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase07.mp4" type="video/mp4">
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
- Reconocer diferentes tipos de sucesiones. 
- Aplicar el principio de inducción.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Sucesiones
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}


 :::{admonition} Definición
:class: tip

 Sea $A$ un conjunto dado. Una \textbf{sucesión} es una función  de la forma $f: D \subseteq \mathbb{N} \to A$.  Así, para cada $n \in D$, $f(n)$ es un elemento de A.  Usualmente escribimos $f(n):=f_n$ o $f(n):=a_n$ para referirnos al término general de la sucesión y $\{f_n\}_{n\in D}$ para la sucesión.
::: 

 :::{admonition} Ejemplo 1
:class: note

Si $A=\mathbb{R}$ entonces diremos que $\{f_n\}_{n\in D}$ es una sucesión real.
- $f:\mathbb{N}\to\mathbb{R}$ dada por $f(n)=\dfrac1{n}$ o $\left\{\dfrac1{n}\right\}_{n\in\mathbb{N}}$.
- $f:\{1,2,3,4,5\}\to\mathbb{R}$ dada por $f(n)=(-1)^n$ o $\{-1,1\}$.
     %\item $A=\left\{y\in\mathbb{R}:y=f(n)=\dfrac{n-1}{n+1}, n\in\mathbb{N}\right\}$.
 
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}

 :::{admonition} Ejemplo 2
:class: note

Si $A=\{p: p~\text{es una proposición}\}$, entonces $\{f_n\}$ es una sucesión de proposiciones, es decir, una función proposicional cuyo dominio es un subconjunto de $\mathbb{N}$.
- $f(n): n^2+n$ es par.
- $\displaystyle \phi(n): 1+2+3+\cdots+n=\frac{n(n+1)}{2}$.
- $q(n): \left(1+\dfrac1{n}\right)^{n}>2$.
 
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





%---------------------------------------------------------------------
## Sucesiones importantes
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Sean $d\in\mathbb{R}$ y $a\in\mathbb{R}$. Una \textbf{progresión aritmética} (P.A.) de primer término $a$ y diferencia $d$ es una sucesión $\{a_n\}_{n\in\mathbb{N}}$ tal que \begin{eqnarray*}a_1&=&a\\ a_{n+1}&=&a_n+d~,~n\in\mathbb{N} \end{eqnarray*} Lo que caracteriza a una P.A. es que la diferencia de dos términos consecutivos de la sucesión es siempre constante igual a $d$.
:::

:::{admonition} Ejemplo
:class: note

La sucesión $1,3,5,7,9,11,\ldots$ es una P.A. de primer término $a=1$ y diferencia $d=2$. 

:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Definición
:class: tip

Sean $r\in\mathbb{R}-\{0\}$ y $a\in\mathbb{R}$. Una \textbf{progresión geométrica} (P.G.) de primer término $a$ y razón $r$ es una sucesión $\{a_n\}_{n\in\mathbb{N}}$ tal que \begin{eqnarray*}a_1&=&a\\ a_{n+1}&=&a_n\cdot r~,~n\in\mathbb{N} \end{eqnarray*}  Lo que caracteriza a una P.G. es que la razón de dos términos consecutivos de la sucesión es siempre constante igual a $r$.
:::

:::{admonition} Ejemplo
:class: note

La sucesión $1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{1}{16},\ldots$ es una P.G. de primer término $a=1$ y razón $r=\frac{1}{2}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





% %---------------------------------------------------------------------
% %## Sucesiones importantes
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   

% :::{admonition} Definición
:class: tip
% 
% Una sucesión $\{a_n\}_{n\in\mathbb{N}}$ es una \textbf{progresión armónica} (P.H.) de primer término $a$ si existe $d\in\mathbb{R}$ tal que \begin{eqnarray*}a_1&=&a\\ a_{n+1}&=&\frac{a_n}{1+a_n\cdot d}~,~n\in\mathbb{N} \end{eqnarray*}
% :::

% :::{admonition} Ejemplo
:class: note
% 
% La sucesión $1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots$ es una P.H. de primer término $a=1$, con $d=1$.
% :::

% 


%---------------------------------------------------------------------
## Primer principio de inducción
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

 :::{admonition} Definición
:class: tip
\textbf{Primer Principio de Inducción}


Sea $\phi(n)$ una función proposicional. Entonces $$\big[\phi(1)\wedge\forall~n\in\mathbb{N}: \big(\phi(n)\Rightarrow\phi(n+1)\big)\big]\Rightarrow\forall~n\in\mathbb{N}:\phi(n)$$
Este principio nos dice que para probar una proposición $\phi(n)$ para todo $n\in\mathbb{N}$, basta con demostrar dos cosas:
- $\phi(1)$.
- $\forall~n\in\mathbb{N}: \phi(n)\Rightarrow\phi(n+1)$.


:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 3
:class: note

Demuestre las siguientes proposiciones:
- $\forall~n \in \mathbb{N}: n(n+1)$ es par.
- $\forall~n \in \mathbb{N}: n^3-n$ es divisible por 6.
- $\forall~n\in\mathbb{N}: 1+2+3+\ldots+n=\dfrac{n(n+1)}{2}.$
- $\forall~n \in \mathbb{N}: 4^n\geq 3n+1$.


:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::







%---------------------------------------------------------------------
%## Principio de inducción
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
  
:::{admonition} Ejemplo 4
:class: note

Demuestre que $$\forall~n\in\mathbb{N}:1+8+27+\cdots+n^3=\frac{n^2(n+1)^2}{4}.$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 5
:class: note

Demuestre que si $a_1=1$ y $a_n=2a_{n-1}+2^{n-1}$ para $n\geq2$, entonces para todo $n\in\mathbb{N}$ se tiene que $a_n=n2^{n-1}$.
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
%       \item El primer principio de inducción se utiliza solamente para proposiciones sobre $\mathbb{N}$, no $\mathbb{R}$.
%       \item Utilizamos este principio principalmente para demostrar propiedades de divisibilidad, sumas, desigualdades (que involucren algún término natural) y fórmulas recursivas. 
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


