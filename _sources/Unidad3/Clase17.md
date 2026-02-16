

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase17.py Clase17` y mueva el archivo resultante a `_static/videos/Clase17.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase17.mp4" type="video/mp4">
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
- Representar geométricamente vectores y sus operaciones. 
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Segmento dirigido
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  




\begin{minipage}[t]{0.5\linewidth}
    
    ```{image} ../Clases/vector1.png
:align: center
:width: 70%
```


:::{admonition} Definición
:class: tip

Dados dos puntos $A$ y $B$ en el plano o en el espacio denotamos por $(A,B)$ al \textbf{segmento dirigido} con punto inicial $A$ y punto final $B$.
:::
 
\begin{minipage}[t]{0.5\linewidth}

El segmento dirigido anterior tiene una \textbf{dirección},  que está dada por la recta que determinan los puntos $A$ y $B$,  tiene un \textbf{sentido} dado,  que identifica en ellos un punto inicial y un punto final.  Podemos observar que $(A,B)\neq (B,A)$ (puesto que tienen sentidos contrarios).  Los segmentos dirigidos tienen también asociado un valor numérico o \textbf{magnitud},  dado por la distancia entre los puntos $A$ y $B$.  


El concepto de vector es algo un poco más general que el de segmento dirigido,  en relación a que ``\textbf{dos segmentos dirigidos que coincidan en dirección, sentido y magnitud, representan el mismo vector}".  Es fundamental comprender esta idea en el análisis vectorial.





%---------------------------------------------------------------------
## Vectores
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
    Lo anterior se formaliza matemáticamente considerando el conjunto de \underline{todos} los segmentos dirigidos del plano o el espacio y estableciendo la siguiente relación $\uparrow$ entre ellos:  $$(A,B)\uparrow (C,D)$$ si los segmentos dirigidos $(A,B)$ y $(C,D)$ tienen igual magnitud, dirección y sentido. 



:::{admonition} Definición
:class: tip
 El \textbf{vector} $\vec{p}$ cuyo punto inicial es $O$ (origen) y final es $P$, corresponde al ``\textbf{representante}" de todos los segmentos dirigidos $(A,B)$ que tienen la misma dirección, sentido y magnitud que el segmento dirigido $(O,P)$,  o sea: $$\vec{p}=[(O,P)]=\{[A,B]:(A,B)\uparrow(O,P)\}.$$
:::
 
\begin{minipage}[t]{0.5\linewidth}
Todos los vectores del siguiente esquema son idénticos ya que tienen igual magnitud, dirección y sentido. El vector $\vec{p}$ es el representante de todos ellos.


\visible<7>{```{image} ../Clases/vector2.png
:align: center
:width: 70%
```}






%---------------------------------------------------------------------
## Suma de vectores
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  




\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Nota 1
:class: tip

El \textbf{vector nulo} $\vec{0}$ corresponde al representante de todos los segmentos dirigidos que comienzan en el punto $A$ y terminan en $A$.
:::

:::{admonition} Nota 2
:class: tip

El segmento dirigido que comienza en el origen $O$ y termina en el punto $P$, es decir el vector $\vec{p}$ suele escribirse como $$\vec{p}=\overrightarrow{OP}$$ y se denomina \textbf{vector posición} del punto $P$.
:::
 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Definición
:class: tip

Consideremos dos vectores $\vec{a}$ y $\vec{b}$. El \textbf{vector suma o adición geométrica}, $\vec{a}+\vec{b}$, es aquel que resulta al unir el origen con el vértice del paralelógramo formado por $\vec{a}$ y $\vec{b}$.
:::


  \visible<6>{```{image} ../Clases/sumavector.png
:align: center
:width: 70%
```} 





%---------------------------------------------------------------------
## Ponderación de vectores y propiedades
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  




\begin{minipage}[t]{0.5\linewidth}
    :::{admonition} Definición
:class: tip

La \textbf{ponderación} del vector $\vec{a}$ por el escalar (número real) $\alpha$ es definida como el nuevo vector $\alpha\vec{a}$ que tiene las siguientes características: si $\alpha>0$ entonces $\alpha\vec{a}$ mantiene el sentido del vector $\vec{a}$, y si $\alpha<0$ entonces $\alpha\vec{a}$ tiene sentido opuesto al vector $\vec{a}$. Si $\alpha=0$ entonces $0\vec{a}=\vec{0}$. 
::: 


  \visible<2-14>{```{image} ../Clases/pondvector.png
:align: center
:width: 70%
``` } 

 
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Propiedades
:class: tip

El conjunto $V$ de todos los vectores geométricos tiene las siguientes propiedades respecto a la adición y ponderación antes definidas: $\forall~\vec{a}, \vec{b}, \vec{c}\in V$ y $\alpha,\beta\in\mathbb{R}$. 


{
- $\vec{a}+\vec{b}\in V$. (Clausura de la adición)
- $(\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})$. (Asociatividad)
- $\vec{a}+\vec{O}=\vec{a}$. (Elemento neutro aditivo)
- $\vec{a}+(-\vec{a})=\vec{0}$. (Inverso aditivo)
- $\vec{a}+\vec{b}=\vec{b}+\vec{a}$. (Conmutatividad)
- $\alpha\vec{a}\in V$. (Clausura de la ponderación)
- $1\vec{a}=\vec{a}$. (Neutro de la ponderación)
- $\alpha(\beta\vec{a})=(\alpha\beta)\vec{a}$. (Asociatividad)
- $(\alpha+\beta)\vec{a}=\alpha\vec{a}+\beta\vec{a}.$ (Distributividad)
- $\alpha(\vec{a}+\vec{b})=\alpha\vec{a}+\alpha\vec{b}$. (Distributividad)

}

:::







%---------------------------------------------------------------------
## Resta de vectores
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  




\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 1
:class: note

A partir de la cuadrícula dada, determine los vectores $2\vec{u}+\vec{v}$ y $\vec{v}-\dfrac{1}{3}\vec{u}$. 

    ```{image} ../Clases/EJ1.png
:align: center
:width: 70%
```

:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Definición
:class: tip

La \textbf{resta} de los vectores $\vec{a}$ y $\vec{b}$ se define como $$\vec{a}-\vec{b}=\vec{a}+(-\vec{b}).$$

\visible<2>{```{image} ../Clases/resta.png
:align: center
:width: 70%
```}

:::





%---------------------------------------------------------------------
%## Resta de vectores
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  




\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Dados los puntos $A$ y $B$ del plano o el espacio, tenemos que el vector que comienza en $A$ y termina en $B$ se puede escribir como una resta de los vectores posición de $A$ y $B$,  es decir $$\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}=\vec{b}-\vec{a}.$$  



\visible<4-5>{```{image} ../Clases/resta2.png
:align: center
:width: 70%
```}

:::
 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Ejemplo 2
:class: note

Sean $A,B,C,D,E$ y $F$, en ese orden, los vértices de un hexágono regular. Demostrar que $$\overrightarrow{AB}+\overrightarrow{AC}+\overrightarrow{AD}+\overrightarrow{AE}+\overrightarrow{AF}=3\overrightarrow{AD}$$
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
%       \item Es fundamental comprender que un vector representa a infinitos objetos que tienen las mismas características: sentido, dirección y magnitud.
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


