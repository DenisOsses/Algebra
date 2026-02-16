

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase11.py Clase11` y mueva el archivo resultante a `_static/videos/Clase11.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase11.mp4" type="video/mp4">
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
- Utilizar y demostrar propiedades de los coeficientes binomiales.
- Aplicar el Teorema del binomio.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Coeficientes binomiales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  
  
Al desarrollar o expandir las potencias de binomio $(a+b)^n$, con $n\in\mathbb{N}_0$, ¿es posible obtener algún patrón numérico? 

\begin{eqnarray*}(a+b)^0 &=& 1\cdot a^0b^0 \\ (a+b)^1 &=& 1\cdot a^1b^0+1\cdot a^0b^1  \\ (a+b)^2 &=& 1\cdot a^2b^0+2\cdot a^1b^1+1\cdot a^0b^2  \\ (a+b)^3 &=& 1\cdot a^3b^0+3\cdot a^2b^1+3\cdot a^1b^2+1\cdot a^0b^3  \\ (a+b)^4 &=& 1\cdot a^4b^0+4\cdot a^3b^1+6\cdot a^2b^2+4\cdot a^1b^3+1\cdot a^0b^4\\  &\vdots&\end{eqnarray*}



%---------------------------------------------------------------------
%## Coeficientes binomiales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

Los coeficientes numéricos de los términos $a^kb^{n-k}$, donde $k=0,1,\ldots,n$, corresponden a los números del \textbf{triángulo de Pascal} 


    ```{image} ../Clases/pascal.png
:align: center
:width: 70%
```




%---------------------------------------------------------------------
%## Coeficientes binomiales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

Los coeficientes numéricos que aparecen en la expansión de las potencias del binomio  

$$(a+b)^n=\underbrace{(a+b)(a+b)(a+b)\cdots(a+b)}_{n~\textrm{veces}}$$ 

consisten en todos los productos posibles que pueden ser formados tomando una letra ($a$ o $b$) de cada factor $(a+b)$.  El número de maneras en que se puede formar el producto $a^kb^{n-k}$ es exactamente igual al número de maneras de elegir $k$ factores (de los $n$ posibles) que contribuyen una $a$, ya que el resto de los factores contribuye una $b$.  El número de maneras de elegir $k$ factores entre $n$ es $C(n,k)=\displaystyle {n\choose k}=\frac{n!}{k!\cdot(n-k)!}$.  Así



%---------------------------------------------------------------------
%## Coeficientes binomiales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  
\begin{eqnarray*}(a+b)^0 &=& {0\choose 0}a^0b^0  \\ (a+b)^1 &=& {1\choose 1} a^1b^0+{1\choose 0}a^0b^1  \\ (a+b)^2 &=& {2\choose 2} a^2b^0+{2\choose 1} a^1b^1+{2\choose 0} a^0b^2  \\ (a+b)^3 &=& {3\choose 3}a^3b^0+{3\choose 2} a^2b^1+{3\choose 1}a^1b^2+{3\choose 0} a^0b^3  \\ (a+b)^4 &=& {4\choose 4} a^4b^0+{4\choose 3}a^3b^1+{4\choose 2} a^2b^2+{4\choose 1} a^1b^3+{4\choose 0} a^0b^4\\ &\vdots&\end{eqnarray*}



%---------------------------------------------------------------------
## Teorema del binomio
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  


\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Teorema del binomio
:class: tip

$\forall~n\in\mathbb{N}_0$ se cumple que $$(a+b)^n=\sum_{k=0}^n{n\choose k}a^kb^{n-k}.$$ 
:::

:::{admonition} Nota
:class: tip

Se tiene que para todo $k=0,1,2,\ldots, n$: $${n\choose n-k}={n\choose k}.$$
:::

\begin{minipage}[t]{0.5\linewidth}

Así, aprovechando esta propiedad simétrica de los coeficientes binomiales, podemos reescribir el Teorema del binomio como:  $$(a+b)^n=\sum_{k=0}^n{n\choose k}a^kb^{n-k}=\sum_{k=0}^n{n\choose k}a^{n-k}b^{k}.$$ 


:::{admonition} Nota
:class: tip

Una propiedad importante de los coeficientes binomiales es que $${n+1\choose k+1}={n\choose k}+{n\choose k+1}~~,~~k=0,1,2,\ldots,n-1.$$  Esta propiedad nos da el resultado de la suma de dos coeficientes consecutivos en el triángulo de Pascal.
:::




%---------------------------------------------------------------------
%## Teorema del binomio
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  
  

\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Ejemplo 1
:class: note

Determine el coeficiente de $x^{10}$ en la expansión del binomio $(x-2)^{10}$.
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 2
:class: note

Encuentre, si existe, el coeficiente que acompa\~{n}a a $x^{50}$ en el desarrollo de $\left(x^{2}-\displaystyle\frac{1}{x^{2}}\right)^{100}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::



\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Ejemplo 3
:class: note

Calcular el valor de 
$$\displaystyle \sum_{k=1}^{701}\left(\begin{array}{c}
701 \\
k\end{array}\right)\frac{1}{7^{k-1}}.$$
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
%       \item El teorema del binomio es la generalización del ``cuadrado de binomio".
%       \item El coeficiente binomial ${n\choose k}$ se puede entender como el número de subconjuntos con $k$ elementos escogidos de un conjunto con $n$ elementos.
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


