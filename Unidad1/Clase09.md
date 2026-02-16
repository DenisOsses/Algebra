

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
- Aplicar el principio de inducción.




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Principio de inducción
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

 :::{admonition} Definición
:class: tip
\textbf{Principio de Inducción}\\


Sea $\phi(n)$ una función proposicional. Entonces $$\big[\phi(1)\wedge\forall~n\in\mathbb{N}: \big(\phi(n)\Rightarrow\phi(n+1)\big)\big]\Rightarrow\forall~n\in\mathbb{N}:\phi(n).$$
Este principio nos dice que para probar una proposición $\phi(n)$ para todo $n\in\mathbb{N}$, basta con demostrar dos cosas:
- $\phi(1)$.
- $\forall~n\in\mathbb{N}: \phi(n)\Rightarrow\phi(n+1)$.


:::



%---------------------------------------------------------------------
%## Principio de inducción
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

:::{admonition} Ejemplo 1
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
  
  
  
:::{admonition} Ejemplo 2
:class: note

Demuestre que $$\forall~n\in\mathbb{N}:1+8+27+\cdots+n^3=\frac{n^2(n+1)^2}{4}.$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Ejemplo 3
:class: note

Demuestre que si $a_1=1$ y $a_n=2a_{n-1}+2^{n-1}$ para $n\geq2$, entonces para todo $n\in\mathbb{N}$ se tiene que $a_n=n2^{n-1}$.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





%==============================================
# Conclusión
%==============================================

# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
- El principio de inducción se utiliza solamente para proposiciones sobre $\mathbb{N}$, no $\mathbb{R}$.
- Utilizamos este principio principalmente para demostrar propiedades de divisibilidad, sumas, desigualdades (que involucren algún término natural) y fórmulas recursivas. 
  



%==============================================
# Asistencia
%==============================================

# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  
  
  \textbf{Solo se considerará la asistencia hasta 5 minutos después de terminada la clase.}
  
  
  ```{image} ../Clases/QR
:align: center
:width: 70%
```
  
  



