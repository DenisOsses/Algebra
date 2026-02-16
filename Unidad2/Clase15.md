

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase15.py Clase15` y mueva el archivo resultante a `_static/videos/Clase15.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase15.mp4" type="video/mp4">
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
- Utilizar las propiedades de las funciones trigonométricas inversas.
- Resolver ecuaciones trigonométricas.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Funciones trigonométricas inversas. Arcoseno
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



Es simple notar, a partir de los gráficos de las funciones seno, coseno y tangente, que ninguna de ellas es inyectiva, por lo que no tienen inversas.  Sin embargo, si restringimos adecuadamente el dominio de cada una, pueden ser inyectivas y, de esta forma, ser invertibles.

:::{admonition} Función inversa de seno
:class: tip

Consideremos $$f:\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\mapsto[-1,1]~~,~~f(x)=\sen(x).$$ En este intervalo $\sen(x)$ es biyectiva y tiene inversa. Su inversa se denomina \textbf{arcoseno} de $x$.  Anotamos $$f^{-1}:[-1,1]\mapsto\left[-\frac{\pi}{2},\frac{\pi}{2}\right]~~,~~f^{-1}(x)=\arcsen(x).$$
:::

\begin{minipage}[t]{0.5\linewidth}



   \visible<5>{```{image} ../Clases/arcoseno.png
:align: center
:width: 70%
```}






%---------------------------------------------------------------------
## Arcocoseno
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



:::{admonition} Función inversa de coseno
:class: tip

Consideremos $$f:[0,\pi]\mapsto[-1,1]~~,~~f(x)=\cos(x).$$ En este intervalo $\cos(x)$ es biyectiva y tiene inversa. Su inversa se denomina \textbf{arcocoseno} de $x$.  Anotamos $$f^{-1}:[-1,1]\mapsto[0,\pi]~~,~~f^{-1}(x)=\arccos(x).$$
:::

\begin{minipage}[t]{0.5\linewidth}



    \visible<3>{```{image} ../Clases/arcocoseno.png
:align: center
:width: 70%
```}






%---------------------------------------------------------------------
## Arcotangente
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



:::{admonition} Función inversa de tangente
:class: tip

Consideremos $$f:\left]-\frac{\pi}{2},\frac{\pi}{2}\right[\mapsto\mathbb{R}~~,~~f(x)=\tan(x).$$ En este intervalo $\tan(x)$ es biyectiva y tiene inversa. Su inversa se denomina \textbf{arcotangente} de $x$.  Anotamos $$f^{-1}:\mathbb{R}\mapsto\left]-\frac{\pi}{2},\frac{\pi}{2}\right[~~,~~f^{-1}(x)=\arctan(x).$$
:::



    \visible<3-5>{```{image} ../Clases/arcotangente.png
:align: center
:width: 70%
```}


\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Ejemplo 1
:class: note

Determine el valor exacto de $\arcsen\left(\dfrac{1}{2}\right)$, $\arctan\left(-1\right)$, $\arccos\left(\cos\dfrac{\pi}{3}\right)$ y $\tan\left(\arcsen\dfrac{\sqrt{2}}{2}\right)$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::



:::{admonition} Ejemplo 2
:class: note

Pruebe que $\forall~x\in[0,1]$: $$\arccos\left(\frac{1-x^2}{1+x^2}\right)=\arcsen\left(\frac{2x}{1+x^2}\right)$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::






%---------------------------------------------------------------------
## Ecuaciones trigonométricas
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



:::{admonition} Definición
:class: tip

Una \textbf{ecuación trigonométrica} es una expresión de la forma $f(x)=0$ donde $f$ es una combinación de funciones trinométricas, para las cuales debemos encontrar los ángulos $x\in\mathbb{R}$ que satisfagan esta ecuación. Lo esencial para resolverlas es recordar la periodicidad de ellas.
:::

:::{admonition} Ejemplo 3
:class: note

Determine todas las soluciones de las ecuaciones dadas:
- $\sen(x)=0$.
- $2\cos(x)-1=0$.
- $\sen^2(x)=2\sen(x)+3$.

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
%       \item Para abordar y comprender correctamente las inversas triginométricas, debe necesariamente tener un manejo adecuado de las funciones trigonométricas básicas.
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


