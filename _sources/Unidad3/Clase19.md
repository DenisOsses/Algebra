

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase19.py Clase19` y mueva el archivo resultante a `_static/videos/Clase19.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase19.mp4" type="video/mp4">
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
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.
- Definir los conceptos de paralelismo entre vectores y producto punto.
    % \item Reconocer los elementos de las diferentes representaciones de rectas y determinar sus ecuaciones. Usar las distintas representaciones de rectas y sus propiedades para resolver problemas geométricos.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Combinación lineal
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  


\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Definición
:class: tip

Un vector $\vec{v}$ es \textbf{combinación lineal} de los vectores $\vec{u_1}$ y $\vec{u_2}$ si existen contantes $\alpha,\beta\in\mathbb{R}$ tales que $$\vec{v}=\alpha\vec{u_1}+\beta\vec{u_2}.$$
:::

:::{admonition} Ejemplo 1
:class: note

Sean $\vec{u}=(3,1)$ y $\vec{v}=(1,2)$. Determine si el vector $\vec{w}=(-1,3)$ es combinación lineal de $\vec{u}$ y $\vec{v}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}

   \visible<3>{```{image} ../Clases/Vect1.png
:align: center
:width: 70%
```}





%---------------------------------------------------------------------
## Vectores paralelos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Definición
:class: tip

Decimos que los vectores $\vec{u}$ y $\vec{v}$ son \textbf{paralelos} si tienen la misma dirección.  Matemáticamente esto significa que un vector es un ponderado o múltiplo del otro, es decir, existe un número $\lambda\in\mathbb{R}$, $\lambda\neq0$, tal que $$\vec{u}=\lambda\vec{v}.$$
:::

:::{admonition} Ejemplo 2
:class: note
Decida si los vectores $\vec{u}=(-1,2)$ y $\vec{v}=(4,-8)$ son paralelos o no.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}
% 
% Observemos la recta $L$ (del plano o espacio) en la figura siguiente: 

% 
%     \visible<5>{```{image} ../Clases/EcVecRecta.png
:align: center
:width: 70%
```}
% 




%---------------------------------------------------------------------
## Producto punto
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Sean $\vec{a}=(a_1,a_2,a_3)$ y $\vec{b}=(b_1,b_2,b_3)$ vectores en el espacio.  El \textbf{producto punto} o \textbf{producto escalar} de $\vec{a}$ con $\vec{b}$ es el número real $\vec{a}\cdot\vec{b}$ definido por  $$\vec{a}\cdot\vec{b}=a_1b_1+a_2b_2+a_3b_3=\sum_{i=1}^3a_ib_i.$$
::: 
Así, para encontrar el producto punto de $\vec{a}$ con $\vec{b}$ se multiplican las coordenadas correspondientes y se suman.  El resultado no es un vector, es un número real.  
:::{admonition} Ejemplo 3
:class: note

Calcule el producto punto entre $\vec{a}=(1,2,3)$ y $\vec{b}=(-1,0,1)$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

 
\begin{minipage}[t]{0.5\linewidth}
:::{admonition} Propiedades
:class: tip
 Si $\vec{a}$, $\vec{b}$ y $\vec{c}$ son vectores en el plano o en el espacio y $\alpha\in\mathbb{R}$, entonces 
[{(a)}]
- $\vec{a}\cdot\vec{a}=||\vec{a}||^2$.
- $\vec{a}\cdot \vec{b}=\vec{b} \cdot \vec{a}$.
- $\vec{a}\cdot (\vec{b}+\vec{c})=\vec{a}\cdot \vec{b}+\vec{a}\cdot \vec{c}$.
- $\alpha(\vec{a}\cdot \vec{b})=(\alpha \vec{a})\cdot \vec{b}=\vec{a}\cdot (\alpha \vec{b})$.
- $\vec{0}\cdot\vec{a}=0$.
- $\vec{a}\cdot \vec{b}=\frac{1}{2}( ||\vec{a}||^2+||\vec{b}||^2-||\vec{b}-\vec{a}||^2)$

:::





% %---------------------------------------------------------------------
% ## Ángulo entre vectores
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 
% 

% \begin{minipage}[t]{0.5\linewidth}
% 
% 
%     ```{image} ../Clases/AnguloVect.png
:align: center
:width: 70%
```
%  
% El producto punto $\vec{a}\cdot \vec{b}$ se puede interpretar geométricamente en términos del ángulo $\theta$ entre $\vec{a}$ y $\vec{b}$, que se define como el ángulo entre los vectores posición asociados a ellos. 
%  
% \begin{minipage}[t]{0.5\linewidth}
% 
% :::{admonition} Teorema
:class: tip
% 
% Si $\theta$ es el ángulo entre $\vec{a}$ y $\vec{b}$ entonces $$\color{red}\boxed{\color{black}\vec{a}\cdot\vec{b}=||\vec{a}||\cdot||\vec{b}||\cos(\theta).}$$ 
% Además, $$\color{red}\boxed{\color{black}\cos(\theta)=\frac{\vec{a}\cdot\vec{b}}{||\vec{a}||\cdot||\vec{b}||}.}$$
% :::
% :::{admonition} Nota
:class: tip
% 
% Si $\theta=0$ o $\theta=\pi$ entonces los vectores son paralelos y $\vec{a}\cdot\vec{b}=\pm||\vec{a}||\cdot||\vec{b}||$, respectivamente.
% :::
% 

% 

% %---------------------------------------------------------------------
% ## Ecuación vectorial de la recta
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 
% 

% \begin{minipage}[t]{0.5\linewidth}
% $P_0$ y $P_1$ son puntos fijos de la recta $L$ y $P$ es un punto variable (móvil sobre la recta).  Notamos que $$\vec{r}=\vec{p_0}+\overrightarrow{P_0P}.$$  Por otro lado, el vector $\overrightarrow{P_0P}$ es paralelo con $\vec{v}$, es decir $\overrightarrow{P_0P}=\lambda\vec{v}$ para algún $\lambda\in\mathbb{R}.$  Luego $${\color{red}\boxed{\color{black}\vec{r}=\vec{p_0}+\lambda\vec{v}}}$$  es conocida como la \textbf{ecuación vectorial de la recta} en el plano o el espacio,  que pasa por el punto $P_0$ y sigue la dirección del vector $\vec{v}$ (\textbf{vector director} de la recta).
%  
% \begin{minipage}[t]{0.5\linewidth}
% :::{admonition} Nota 1
:class: tip
% 
% El vector director $\vec{v}$ puede ser cualquier vector que siga o indique la dirección de la recta $L$; así que no es necesario que esté explícitamente sobre dicha recta, basta con un vector paralelo a ella.
% ::: 

% :::{admonition} Nota 2
:class: tip
% 
% Podemos visualizar la ecuación de la recta en el plano con punto móvil $P$ y vector dirección $\vec{v}$ en el siguiente enlace de \href{https://www.geogebra.org/m/Tn8n4Q5a}{\textbf{Geogebra}} y el siguiente \href{https://www.geogebra.org/m/R28FMcuF}{\textbf{enlace}} para la recta en el espacio.
% :::
% 

% 

% %---------------------------------------------------------------------
% ## Ecuación paramétrica y cartesiana de la recta
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 
% 

% \begin{minipage}[t]{0.5\linewidth}
% Si escribimos los vectores anteriores en coordenadas:  $\vec{r}=(x,y,z)$, $\vec{p_0}=(x_0,y_0,z_0)$, \newline $\vec{v}=(a,b,c)$,  entonces podemos deducir la ecuación \textbf{paramétrica} de la recta \begin{eqnarray*}x&=&x_0+a\lambda\\ y&=&y_0+b\lambda~~~~~~~~,~~~~\lambda\in\mathbb{R}\\ z&=&z_0+c\lambda\end{eqnarray*}  y la ecuación \textbf{cartesiana} de la recta  $$\frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}\quad,\quad a,b,c\neq0$$
%  
% \begin{minipage}[t]{0.5\linewidth}
% 
% :::{admonition} Ejemplo 3
:class: note
% 
% Determinar en cada caso un vector director para la recta indicada y una ecuación vectorial de esa recta que: 

% 
% 
%     \item Contiene a los puntos $A(3,9)$ y $B(-5,1)$.
%     %\item Recta que contiene al punto $C(12,1)$ y es paralela a la recta $(x,y)=(1,1)+\lambda(4,-5)$, $\lambda \in \mathbb{R}$.
%     %\item Recta que contiene al punto $C(0,4)$ y es perpendicular a la recta $(x,y)=(7,-1)+\lambda(3,2)$, $\lambda \in\mathbb{R}$.
%     \item Contiene a los dos puntos $D(1,-2,1)$ y $E(1,-1,1)$.
%     \item Contiene al punto $G(0,1,-2)$ y es paralela a la recta $(x,y,z)=(2,0,1)+\lambda(3,1,0)$, $\lambda \in\mathbb{R}$.
%     \item Pasa por $P(1,0,1)$ y que corta a la recta de ecuación vectorial $\vec{r}=(1, 2,-1)+\lambda(2, 1,-2)$, en los puntos situados a dos unidades de distancia de $P_0(1, 2,-1)$.
% 

% :::
% 

% 


% %==============================================
% # Conclusión
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   
%   
%       \item La definiciones para vectores en $\mathbb{R}^3$ y $\mathbb{R}^2$ son análogas. En $\mathbb{R}^3$, basta con anular la tercera coordenada en las expresiones anteriores para obtener las definiciones en $\mathbb{R}^2$.
%       \item Un buen ejercicio es probar que la ecuación vectorial de la recta en el plano es equivalente a la ecuación lineal en el plano.
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


