

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario
  \setbeamertemplate{section in toc}[sections numbered]
  \tableofcontents%[hideallsubsections]


%==============================================
# Objetivos de hoy
%==============================================
%## Charts
# \insertsectionhead
  ### \insertsubsectionhead
- Caracterizar la perpendicularidad de rectas en el plano y en el espacio.
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.




%==============================================
# Contenidos
%==============================================

% %---------------------------------------------------------------------
% ## Paralelismo de rectas
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 

% :::{admonition} Definición
:class: tip
% 
% Dos rectas en el espacio (o en el plano) son paralelas si y solo si sus vectores directores son paralelos y dichas rectas no se cortan.  Luego, rectas coincidentes no son paralelas.
% :::

% :::{admonition} Ejemplo 1
:class: note
% 
% % Determine, en cada caso, si los tres puntos dados son colineales.
% Determine si los tres puntos dados son colineales: $P(1, 2,-3), Q(3,-4, 2)$ y $R(1, 1, 2)$
% % 
% % \item $P(1, 2,-3), Q(3,-4, 2)$ y $R(1, 1, 2)$.
% % \item $P(1, 2,-3), Q(3,-4, 2)$ y $R(-1, 8,-8)$.
% % 
% :::

% :::{admonition} Ejemplo 2
:class: note
% 
% ¿Es paralela la recta $\displaystyle \frac{x-1}{2}=\frac{y-3}{3}=\frac{z-4}{1}$ con $x=4t, y=6t, z=2t$, $t\in\mathbb{R}$?
% :::

% 

%---------------------------------------------------------------------
## Perpendicularidad de rectas. Vector Proyección
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip

Dos rectas en el espacio (o en el plano) son perpendiculares si y solo si sus vectores directores son perpendiculares y si dichas rectas se cortan en un punto. 
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

:::{admonition} Ejemplo 1
:class: note

¿Es perpendicular la recta $\displaystyle \vec{r}=(1,0,1)+\lambda(1,2,3)$, $\lambda\in\mathbb{R}$, con $x=1+t, y=t, z=1-4t$, $t\in\mathbb{R}$?
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

:::{admonition} Definición
:class: tip

El vector $\lambda\vec{b}$ se denomina \textbf{vector proyección ortogonal} de $\vec{x}$ sobre $\vec{b}$ y se denota por $P_{\vec{b}}(\vec{x})$.
:::
 
\begin{minipage}[t]{0.5\linewidth}
\visible<4-5>{```{image} ../Clases/Proyeccion1.png
:align: center
:width: 70%
```}

Los vectores $\vec{b}$ e $\vec{y}$ son ortogonales en el punto $B$. El vector $\overrightarrow{AB}=\lambda\vec{b}$ es un ponderado de $\vec{b}$ (ya que son paralelos).




% %---------------------------------------------------------------------
% %## Perpendicularidad de rectas
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 

% :::{admonition} Ejemplo 3
:class: note
% 
% Considere las rectas 
% \begin{eqnarray*}
% \ell_1 &:& (x, y, z) = (1, 3,-2) + t(4,5,-3),~~t\in\mathbb{R}\\ 
% \ell_2 &:& \dfrac{x-2}{2}=\dfrac{y+3}{3}=\dfrac{5-z}{2}
% \end{eqnarray*}

% 
% 
% \item Determine si las rectas $\ell_1$ y $\ell_2$ se intersectan.
% \item Encuentre una recta $\ell$ que sea paralela a la recta $\ell_1$ y que pase por el punto $(-2, 3, 5)$.
% \item Determine una recta $\ell$ que sea perpendicular a la recta $\ell_2$ y que pase por el punto $(2, 0, 1)$.
% 
% :::

% 

%---------------------------------------------------------------------
## Vector proyección. Propiedades
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}
%
Notamos que 

$$\lambda\vec{b}+\vec{y}=\vec{x}.$$ Como el vector $\vec{y}$ es ortogonal con $\vec{b}$, tenemos que $\vec{y}\cdot\vec{b}=0$.  Luego, si a la igualdad anterior le realizamos un producto punto con $\vec{b}$, obtenemos que $$\lambda=\frac{\vec{x}\cdot\vec{b}}{\vec{b}\cdot\vec{b}}=\frac{\vec{x}\cdot\vec{b}}{||\vec{b}||^2}.$$ Por lo tanto 

$$\color{red}\boxed{\color{black}P_{\vec{b}}(\vec{x})=\left(\frac{\vec{x}\cdot\vec{b}}{||\vec{b}||^2}\right)\vec{b}}$$ 

:::{admonition} Nota
:class: tip

El vector $\vec{y}=\vec{x}-P_{\vec{b}}(\vec{x})$ se denomina \textbf{complemento ortogonal} y es muy útil para determinar distancias.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

 
\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Ejemplo 2
:class: note

Si $\vec{u}=(2,4)$ y $\vec{v}=(5,3)$, determine $P_{\vec{v}}(\vec{u})$ y $P_{\vec{u}}(\vec{v})$. Dibuje estos vectores y sus complementos ortogonales.
::: 

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Propiedades
:class: tip 

Si $\displaystyle P_{\vec{b}}(\vec{x})$ denota la proyección ortogonal de $\vec{x}$ sobre $\vec{b}$ entonces:  
[{(1)}]
- $\displaystyle P_{\vec{b}}(\vec{b})=\vec{b}$.
- Si $\vec{a}$ es cualquier vector perpendicular al vector $\vec{b}$ entonces $\displaystyle P_{\vec{b}}(\vec{a})=\vec{0}$.
- $\displaystyle P_{\vec{b}}(\lambda\vec{x})=\lambda \displaystyle P_{\vec{b}}(\vec{x})$.
- $\displaystyle P_{\vec{b}}(\vec{x}+\vec{y})=\displaystyle P_{\vec{b}}(\vec{x})+\displaystyle P_{\vec{b}}(\vec{y})$


::: 

:::{admonition} Ejemplo 3
:class: note

Considere la recta $L:\frac{x-1}{2}=y-2=\frac{z-3}{2}.$ Encuentre la ecuación de la recta perpendicular a $L$ que pasa por el punto $(1,2,1)$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::






% %---------------------------------------------------------------------
% %## Vector proyección
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
% 

% :::{admonition} Ejemplo 5
:class: note
% 
% Considere la recta $$L:\frac{x-1}{2}=y-2=\displaystyle\frac{z-3}{2}.$$ Encuentre la ecuación de la recta perpendicular a $L$ que pasa por el punto $(1,2,1)$.
% :::

% % :::{admonition} Ejemplo 6
:class: note
% % 
% % Calcule la distancia más corta desde el punto $(2,6)$ a la recta que pasa por el origen y tiene vector director a $\vec{v}=(7,4)$.
% % :::

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
%       \item A veces existen distintas definiciones de perpendicularidad de 2 rectas en el espacio. Acá elegimos la que requiere ortogonalidad de sus vectores directores e intersección entre ellas.
%       % \item Un excelente ejercicio es realizar el ejemplo 3, parte (3), usando vector proyección y complemento ortogonal.
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


