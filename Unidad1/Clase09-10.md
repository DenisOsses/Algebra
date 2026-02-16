

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase09.py Clase09` y mueva el archivo resultante a `_static/videos/Clase09.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase09.mp4" type="video/mp4">
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
- Definir y calcular sumas aplicando sus propiedades.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Sumatorias. Propiedades
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
  
:::{admonition} Definición
:class: tip

Considere la sucesión $\{f(k)\}_{k\in\mathbb{N}}=\{a_k\}_{k\in\mathbb{N}}$. La suma de los $n$ primeros términos de esta sucesión se denomina \textbf{sumatoria} de tales términos.  Anotamos $$\sum_{k=1}^n a_k=a_1+a_2+\cdots+a_n.$$  Notamos que $$\sum_{k=1}^1 a_k=a_1~~,~~\sum_{k=1}^{n+1} a_k=\left(\sum_{k=1}^{n}a_k\right)+a_{n+1}.$$
:::

\begin{minipage}[t]{0.5\linewidth}
  
  
:::{admonition} Propiedades iniciales
:class: tip
- $\displaystyle\sum_{k=1}^{n}c=\underbrace{c+c+c+\cdots+c}_{n~\text{veces}}=nc,$ donde $c$ es constante.
- $\displaystyle\sum_{k=1}^{n}k=1+2+3+\cdots+n=\frac{n(n+1)}{2}$.
- $\displaystyle\sum_{k=1}^{n}k^2=1^2+2^2+3^2+\cdots+n^2=\frac{n(n+1)(2n+1)}{6}$.
- $\displaystyle\sum_{k=1}^{n}k^3=1^3+2^3+3^3+\cdots+n^3=\frac{n^2(n+1)^2}{4}$.

:::




%---------------------------------------------------------------------
## Propiedades
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Sumas importantes
:class: tip
- \textbf{Aritmética}: $\displaystyle\sum_{k=1}^{n}\left(a+kd\right)=an+d\cdot\frac{n(n+1)}{2}$, donde $a,d$ son constantes.
- \textbf{Geométrica}: $\displaystyle\sum_{k=1}^{n}r^{k}=r\cdot\dfrac{1-r^n}{1-r}$, si $r\neq1$.
- \textbf{Telescópica}:  $\displaystyle\sum_{k=m}^{n}(a_{k}-a_{k+1})=a_{m}-a_{n+1},$ con $ 1 \leq m\leq n$

:::

\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Propiedades
:class: tip
- \textbf{Linealidad}: $\displaystyle\sum_{k=1}^{n}(a_{k}+b_{k})=\displaystyle\sum_{k=1}^{n}a_{k}+\displaystyle\sum_{k=1}^{n}b_{k}$
- \textbf{Asociatividad}: $\displaystyle\sum_{k=1}^{n}a_{k}=\displaystyle\sum_{k=1}^{m}a_{k}+\displaystyle\sum_{k=m+1}^{n}a_{k} , \ \mbox{con} \ 1 \leq m < n$.
- \textbf{Factorización}: $\displaystyle\sum_{k=1}^{n}ca_{k}=c\displaystyle\sum_{k=1}^{n}a_{k}, \ \mbox{con} \ c \ \mbox{constante real}.$
- \textbf{Cambio de índice}: $\displaystyle\sum_{k=m}^{n}a_{k}=\displaystyle\sum_{k=m-l}^{n-l}a_{k+l}=\displaystyle\sum_{k=m+l}^{n+l}a_{k-l}, \ \mbox{con} \ l \leq m<n$.  



:::




%---------------------------------------------------------------------
## Ejemplos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 1
:class: note

Calcule: $\displaystyle\sum_{k=11}^{20}(2-k)$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 2
:class: note

Pruebe que: $\displaystyle\sum_{k=3}^{20}\ln\left(\frac{k}{k+1}\right)=\ln(3)-\ln(21)$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 3
:class: note

Demuestre la fórmula de suma geométrica generalizada: $\displaystyle\sum_{k=m}^{n}r^k=\frac{r^m-r^{k+1}}{1-r}$, $r\neq1$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Ejemplo 4
:class: note

Calcular $\displaystyle\sum_{k=1}^{100}a_{k}$, donde $\{a_{k}\}_{k\in\mathbb{N}}$ es la sucesi\'on definida por:
$$a_{k} = \; \left\{\begin{array}{ccl}
\displaystyle\frac{2^{k}+(-2)^{k}}{3^{k+1}} & \mbox{si}& 1\leq k\leq 50\\
\\
\sqrt{k+2}-\sqrt{k} & \mbox{si}& k>50 \\
\end{array}\right.$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 5
:class: note

Considere la sucesión $\{a_n\}_{n \in \mathbb{N}}$, definida por $a_n=n^2+n$.  Escriba la suma  $a_{2}+a_{4}+a_{6}+\cdots+a_{200}$ \ usando el símbolo de sumatoria $\sum$ y calcule el valor de dicha suma.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





%---------------------------------------------------------------------
%## Sumatorias
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo 6
:class: note

A una paciente se le administran 10 unidades de cierta medicina diariamente. El organismo, después de 24 horas, elimina el $20\%$ de la
medicina que se tiene en el cuerpo cada día. La droga es peligrosa para el organismo si se acumulan muchas unidades en el cuerpo; de hecho, es mortal si en el cuerpo hay 60 unidades de medicina o más. Determine si es posible administar indefinidamente la medicina a la paciente
sin correr riesgo de muerte
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
%       \item Las sumatorias son adiciones de elementos de una sucesión generada por una patrón o fórmula $f(k)=a_k$. Su símbolo $\sum$ es una forma abreviada de escribir dicha suma.
%   

% 

% % %==============================================
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


